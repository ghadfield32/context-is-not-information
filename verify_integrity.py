"""Fresh-clone integrity check for the Context Is Not Information development package.

Run this from a clean clone of ``full-paper-development``, not from a working
copy on the authoring machine. On a Windows checkout the worktree can carry CRLF
line endings while ``.gitattributes`` declares ``* text=auto eol=lf``, in which
case a local check cannot tell a correct hash from a contaminated one. A clone
always receives exactly the stored bytes.

    python verify_integrity.py            # verify the current directory
    python verify_integrity.py <clone-dir>

Exit status is 0 only when every check passes.

Declared exclusions, stated in both files' own metadata:

* ``SHA256SUMS`` excludes only itself. Every other tracked file is listed.
* ``GIT_MANIFEST.json`` excludes itself, which is unavoidable, and also excludes
  ``SHA256SUMS``, which records its sha256; including it would be circular.

Neither file can record the hash of the commit that contains it. Both describe
``snapshot_base_commit``, and are committed in that commit's child.

The retracted-value check is deliberately not a bare grep: see
``RETRACTION_MARKERS`` for why a check that fires on its own documentation is
worse than no check.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
import sys

RETRACTED_PATTERN = r"43\.94|41\.43([^0-9]|$)"

# A bare grep for the retracted values would fire on the passages that document
# the retraction, producing a permanently red check that readers learn to
# ignore. The standing invariant is weaker and sharper: these values must never
# appear as results again. So a hit is a failure only when its line carries no
# retraction marker. A reintroduced 43.94 in RESULTS.md matches nothing here and
# fails, which is the case worth catching.
RETRACTION_MARKERS = (
    "retract",
    "no longer",
    "does not appear",
    "appear nowhere",
    "replaced",
    "unverifiable",
    "not appear anywhere",
)


def git(root: pathlib.Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=True
    ).stdout


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    failures: list[str] = []

    tracked = set(git(root, "ls-files").split())

    # 1. SHA256SUMS verifies entry by entry.
    sums_file = root / "SHA256SUMS"
    declared: dict[str, str] = {}
    for line in sums_file.read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, rel = line.split("  ", 1)
            declared[rel.strip()] = digest.strip()

    ok, bad, missing = [], [], []
    for rel, digest in declared.items():
        path = root / rel
        if not path.exists():
            missing.append(rel)
        elif sha256(path) != digest:
            bad.append(rel)
        else:
            ok.append(rel)

    print(f"SHA256SUMS      : {len(ok)}/{len(declared)} verified")
    if missing:
        print(f"  MISSING       : {missing}")
        failures.append("missing files")
    if bad:
        print(f"  MISMATCH      : {bad}")
        failures.append("hash mismatch")

    uncovered = sorted(tracked - set(declared) - {"SHA256SUMS"})
    print(f"  coverage      : {'ok' if not uncovered else 'FAIL'} "
          f"({len(declared)} listed / {len(tracked)} tracked)")
    if uncovered:
        print(f"  unlisted      : {uncovered}")
        failures.append("sums coverage")

    # 2. GIT_MANIFEST.json maps every remaining tracked blob.
    manifest_path = root / "GIT_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    excluded = {"GIT_MANIFEST.json", "SHA256SUMS"}
    actual = {rel: git(root, "hash-object", rel).strip()
              for rel in sorted(tracked - excluded)}

    manifest_ok = manifest["files"] == actual
    print(f"GIT_MANIFEST    : {'ok' if manifest_ok else 'FAIL'} "
          f"({len(manifest['files'])} blobs)")
    if not manifest_ok:
        print(f"  only in manifest: {sorted(set(manifest['files']) - set(actual))}")
        print(f"  only in git     : {sorted(set(actual) - set(manifest['files']))}")
        print(f"  blob mismatch   : "
              f"{sorted(k for k in set(actual) & set(manifest['files']) if actual[k] != manifest['files'][k])}")
        failures.append("git manifest")

    if set(manifest["files"]) | excluded != tracked:
        print(f"  coverage      : FAIL -> {sorted(tracked - set(manifest['files']) - excluded)}")
        failures.append("manifest coverage")
    else:
        print(f"  coverage      : ok (every tracked file, {len(excluded)} declared exclusions)")

    # 3. The two files must agree about each other.
    listed = declared.get("GIT_MANIFEST.json")
    xlink = listed == sha256(manifest_path)
    print(f"cross-link      : {'ok' if xlink else 'FAIL'} "
          f"(SHA256SUMS records GIT_MANIFEST.json sha256)")
    if not xlink:
        failures.append("cross-link")

    # 4. The snapshot claim resolves as a real commit in this repository.
    base = manifest["snapshot_base_commit"]
    resolved = subprocess.run(
        ["git", "rev-parse", "--verify", f"{base}^{{commit}}"],
        cwd=root, capture_output=True, text=True,
    )
    base_ok = resolved.returncode == 0
    head = git(root, "rev-parse", "HEAD").strip()
    print(f"snapshot_base   : {'ok' if base_ok else 'FAIL'} {base[:7]} "
          f"(HEAD {head[:7]}{'' if base == head else ', parent of the snapshot commit'})")
    if not base_ok:
        failures.append("snapshot base")

    # 5. The retracted values must never reappear as results.
    grep = subprocess.run(
        ["git", "grep", "-n", "-i", "-E", RETRACTED_PATTERN],
        cwd=root, capture_output=True, text=True,
    )
    hits = [line for line in grep.stdout.splitlines() if line.strip()]
    unmarked = [
        line for line in hits
        if not any(marker in line.lower() for marker in RETRACTION_MARKERS)
    ]
    print(f"retracted values: {'ok' if not unmarked else 'FAIL'} "
          f"({len(hits)} documented mention(s), none asserted as a result)")
    if unmarked:
        print("  UNMARKED OCCURRENCE(S) -- value presented without a retraction note:")
        for line in unmarked:
            print(f"    {line}")
        failures.append("retracted values")

    print()
    print("VERDICT:", "ALL PASS" if not failures else f"FAIL -> {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
