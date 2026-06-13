# mypy

> Type check Python code.
> More information: <https://mypy.readthedocs.io/en/stable/running_mypy.html>.

- Type check a specific file:

`mypy {{path/to/file.py}}`

- Type check a specific module:

`mypy {{[-m|--module]}} {{module_name}}`

- Type check a specific package:

`mypy {{[-p|--package]}} {{package_name}}`

- Type check a string of code:

`mypy {{[-c|--command]}} "{{code}}"`

- Ignore missing imports:

`mypy --ignore-missing-imports {{path/to/file_or_directory}}`

- Show detailed error messages:

`mypy {{[--tb|--show-traceback]}} {{path/to/file_or_directory}}`

- Specify a custom configuration file:

`mypy --config-file {{path/to/config_file}}`

- Display help:

`mypy {{[-h|--help]}}`
