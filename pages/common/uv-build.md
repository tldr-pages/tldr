# uv build

> Build Python packages into source distributions and wheels.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-build>.

- Build a package in the current directory:

`uv build`

- Build a package from a specific directory:

`uv build {{path/to/directory}}`

- Build only a wheel (skip source distribution):

`uv build --wheel`

- Build only a source distribution (skip wheel):

`uv build --sdist`

- Build and output to a specific directory:

`uv build {{[-o|--out-dir]}} {{path/to/output}}`

- Build a specific package in a workspace:

`uv build --package {{package_name}}`

- Build all packages in the workspace:

`uv build {{[--all|--all-packages]}}`

- Build with a specific Python interpreter:

`uv build {{[-p|--python]}} {{python3.11}}`
