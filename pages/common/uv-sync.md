# uv sync

> Update the project's environment to match the lockfile.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-sync>.

- Sync the project environment with the lockfile:

`uv sync`

- Sync and include all optional dependencies:

`uv sync --all-extras`

- Sync with specific optional dependencies:

`uv sync --extra {{extra_name}}`

- Sync only development dependencies:

`uv sync --only-dev`

- Sync excluding development dependencies:

`uv sync --no-dev`

- Sync specific dependency groups:

`uv sync --group {{group_name}}`

- Check if environment is already synchronized (no changes):

`uv sync --check`

- Preview what would be synced without making changes:

`uv sync --dry-run`
