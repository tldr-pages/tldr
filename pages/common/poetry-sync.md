# poetry sync

> Syncs your project’s environment with the `poetry.lock` file.
> These commands reference `poetry.lock` files in your Poetry configuration directory.
> More information: <https://python-poetry.org/docs/cli/#sync>.
> See also <https://python-poetry.org/docs/managing-dependencies/#group-include-pep735> and <https://python-poetry.org/docs/pyproject/#extras>.

- Syncs your project’s environment with the `poetry.lock` file:

`poetry sync`

- Excludes one or more dependency groups for the installation:

`poetry sync --without test,docs`

- Selects optional dependency groups:

`poetry sync --with test,docs`

- Installs all dependency groups including optional groups:

`poetry sync --all-groups`

- Installs specific dependency groups:

`poetry sync --only test,docs`

- Installs project without dependencies:

`poetry sync --only-root`

- Specifies extras to install:

`poetry sync -E |—extras`

- Installs all defined extras:

`poetry sync --all-extras`

- Skips the defaulted package installation for your project:

`poetry sync --no-root`

- Skips directory path dependencies:

`poetry sync --no-directory`

- Compiles source files to bytecode during installation

`poetry sync --compile`