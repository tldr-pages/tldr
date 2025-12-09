# uv lock

> Update the project's lockfile.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-lock>.

- Create or update the project's lockfile:

`uv lock`

- Check if the lockfile is up-to-date without updating it:

`uv lock --check`

- Assert that a lockfile exists without checking if it's current:

`uv lock --check-exists`

- Preview what would be locked without writing the lockfile:

`uv lock --dry-run`

- Lock a specific Python script instead of the current project:

`uv lock --script {{path/to/script.py}}`

- Upgrade all packages to their latest compatible versions:

`uv lock --upgrade`

- Upgrade only specific packages:

`uv lock --upgrade-package {{package1}} --upgrade-package {{package2}}`
