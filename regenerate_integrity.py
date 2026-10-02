"""Regenerate the DPV development-branch integrity files in dependency order.

Order matters and is the reason this is a script rather than two inline steps:

1. GIT_MANIFEST.json is written first, excluding itself and SHA256SUMS.
2. SHA256SUMS is written second, so the sha256 it records for GIT_MANIFEST.json
   describes the manifest's final bytes.

Writing them the other way round leaves the recorded manifest hash one revision
stale, which is what happened and what this script exists to prevent.

Both files hash COMMITTED bytes. Run ``git add -A`` and re-run this script if
any file changed, because a Windows worktree may hold CRLF while Git stores LF.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
import sys

EXCLUDED_FROM_MANIFEST = ("GIT_MANIFEST.json", "SHA256SUMS")

SCOPE_NOTE = (
    "Blob map of every tracked file on full-paper-development at "
    "snapshot_base_commit. Excludes GIT_MANIFEST.json (cannot contain its own "
    "hash) and SHA256SUMS (which records this file's sha256, so including it "
    "would be circular). SHA256SUMS excludes only itself, matching the PMI and "
    "E1 packages. Together the two files cover every tracked file with exactly "
    "those two documented exclusions. Neither file can name the commit that "
    "contains it, so both describe snapshot_base_commit and are committed in "
    "that commit's child."
)


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

    def git(*args: str) -> str:
        return subprocess.run(
            ["git", *args], cwd=root, capture_output=True, text=True, check=True
        ).stdout

    tracked = sorted(git("ls-files").split())
    head = git("rev-parse", "HEAD").strip()

    # Step 1: manifest.
    blobs = {
        rel: git("hash-object", rel).strip()
        for rel in tracked
        if rel not in EXCLUDED_FROM_MANIFEST
    }
    manifest = {
        "schema": "dpv.git_manifest.v1",
        "branch": "full-paper-development",
        "snapshot_base_commit": head,
        "generated_from": "git hash-object over tracked files at HEAD",
        "scope_note": SCOPE_NOTE,
        "files": dict(blobs),
    }
    (root / "GIT_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline=""
    )
    print(f"GIT_MANIFEST.json : {len(blobs)} blobs, base {head[:7]}")

    # Step 2: sums, last.
    lines = [
        f"{hashlib.sha256((root / rel).read_bytes()).hexdigest()}  {rel}"
        for rel in tracked
        if rel != "SHA256SUMS"
    ]
    (root / "SHA256SUMS").write_text(
        "\n".join(lines) + "\n", encoding="utf-8", newline=""
    )
    print(f"SHA256SUMS        : {len(lines)} entries")
    print(f"  records manifest: "
          f"{hashlib.sha256((root / 'GIT_MANIFEST.json').read_bytes()).hexdigest()[:16]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
