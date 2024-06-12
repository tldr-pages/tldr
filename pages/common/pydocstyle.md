# pydocstyle

> Statically check Python scripts for compliance with Python docstring conventions.
> More information: <https://www.pydocstyle.org/en/latest/>.

- Analyze a Python script or all the Python scripts in a specific directory:

`pydocstyle {{file.py|path/to/directory}}`

- Show an explanation of each error:

`pydocstyle {{-e|--explain}} {{file.py|path/to/directory}}`

- Show debug information:

`pydocstyle {{-d|--debug}} {{file.py|path/to/directory}}`

- Display the total number of errors:

`pydocstyle --count {{file.py|path/to/directory}}`

- Use a specific configuration file:

`pydocstyle --config {{path/to/config_file}} {{file.py|path/to/directory}}`

- Ignore one or more errors:

`pydocstyle --ignore {{D101,D2,D107,...}} {{file.py|path/to/directory}}`

- Check for errors from a specific convention:

`pydocstyle --convention {{pep257|numpy|google}} {{file.py|path/to/directory}}`
