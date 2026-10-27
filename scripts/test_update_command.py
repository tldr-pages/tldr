# SPDX-License-Identifier: MIT

from pathlib import Path
import shutil
import subprocess
import sys

import pytest


@pytest.mark.parametrize("directory_name", ["tldr", "tldr_clone"])
@pytest.mark.parametrize("dry_run", [False, True])
def test_update_command_from_outside_repository(
    tmp_path, monkeypatch, directory_name, dry_run
):
    root = tmp_path / directory_name
    scripts = root / "scripts"
    scripts.mkdir(parents=True)
    source = Path(__file__).resolve().parent
    for filename in ("update-command.py", "_common.py"):
        shutil.copyfile(source / filename, scripts / filename)

    monkeypatch.delenv("TLDR_ROOT", raising=False)
    if directory_name != "tldr":
        monkeypatch.setenv("TLDR_ROOT", str(root))

    pages = []
    for directory, value in (("pages", "value"), ("pages.zh", "值")):
        page = root / directory / "common" / "demo.md"
        page.parent.mkdir(parents=True)
        page.write_text(f"# demo\n\n`demo {{{{{value}}}}}`\n", encoding="utf-8")
        pages.append(page)

    result = subprocess.run(
        [
            sys.executable,
            str(scripts / "update-command.py"),
            "common",
            "demo",
            "-c",
            "demo {{}}",
            "-u",
            "demo --new {{}}",
        ]
        + (["--dry-run"] if dry_run else []),
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    if dry_run:
        assert pages[0].read_text(encoding="utf-8") == "# demo\n\n`demo {{value}}`\n"
        assert pages[1].read_text(encoding="utf-8") == "# demo\n\n`demo {{值}}`\n"
    else:
        assert (
            pages[0].read_text(encoding="utf-8") == "# demo\n\n`demo --new {{value}}`\n"
        )
        assert pages[1].read_text(encoding="utf-8") == "# demo\n\n`demo --new {{值}}`\n"
