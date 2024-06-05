# mypy

> Type check Python code.
> More information: <https://mypy.readthedocs.io/en/stable/running_mypy.html>.

- Type check a specific file:

`mypy {{path/to/file.py}}`

- Type check a specific [m]odule:

`mypy -m {{module_name}}`

- Type check a specific [p]ackage:

`mypy -p {{package_name}}`

- Type check a string of code:

`mypy -c "{{code}}"`

- Ignore missing imports:

`mypy --ignore-missing-imports {{path/to/file_or_directory}}`

- Show detailed error messages:

`mypy --show-traceback {{path/to/file_or_directory}}`

- Specify a custom configuration file:

`mypy --config-file {{path/to/config_file}}`

- Display [h]elp:

`mypy -h`
