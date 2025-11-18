# conda package

> Create low-level conda packages.
> More information: <https://docs.conda.io/projects/conda/en/stable/commands/package.html>.

- Get conda package from file:

`conda package {{[-w|--which]}} {{path/to/file}}`

- Remove all untracked files:

`conda package {{[-r|--reset}}`

- Display all untracked files:

`conda package {{[-u|--untracked]}}`

- Designate package name of the package being created:

`conda package --pkg-name {{name}}`

- Designate package version of the package being created:

`conda package --pkg-version {{version}}`

- Designate package build number of the package being created:

`conda package --pkg-build {{build_number}}`
