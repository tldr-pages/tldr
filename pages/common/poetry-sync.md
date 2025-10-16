# poetry sync

> Syncs your project's environment with the `poetry.lock` file.
> More information: <https://python-poetry.org/docs/cli/#sync>.

- Sync your project’s environment with the `poetry.lock` file:

`poetry sync`

- Exclude one or more dependency groups for the installation:

`poetry sync --without {{test|docs|...}}`

- Select optional dependency groups:

`poetry sync --with {{test|docs|...}}`

- Install all dependency groups including optional groups:

`poetry sync --all-groups`

- Install specific dependency groups:

`poetry sync --only {{test|docs|...}}`

- Install project without dependencies:

`poetry sync --only-root`

- Specify extras to install:

`poetry sync {{[-E|--extras]}}`

- Skip the defaulted package installation for your project:

`poetry sync --no-root`
