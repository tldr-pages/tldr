# memray

> Profile memory usage of a Python application.
> More information: <https://github.com/bloomberg/memray#usage>.

- Run a Python file and track memory usage:

`memray run {{path/to/file}}.py`

- Run a [m]odule and track memory usage:

`memray run -m {{module_name}}`

- Specify an output name:

`memray run {{[-o|--output]}} {{path/to/output_file}}.bin {{path/to/file}}.py`

- Display a summary of memory usage:

`memray summary {{path/to/file}}.bin`

- Generate an HTML flamegraph:

`memray flamegraph {{path/to/file}}.bin`
