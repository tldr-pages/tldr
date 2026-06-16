# pyinstaller

> Bundle a Python application and its dependencies into a single package.
> More information: <https://pyinstaller.org/en/stable/man/pyinstaller.html>.

- Bundle a Python script into a one-folder bundle (output goes to `dist/`):

`pyinstaller {{path/to/script.py}}`

- Bundle a Python script into a single executable file:

`pyinstaller {{[-F|--onefile]}} {{path/to/script.py}}`

- Bundle a GUI application without opening a console window:

`pyinstaller {{[-w|--windowed]}} {{path/to/script.py}}`

- Set the name of the bundled executable:

`pyinstaller {{[-n|--name]}} {{app_name}} {{path/to/script.py}}`

- Set a custom icon for the executable:

`pyinstaller {{[-i|--icon]}} {{path/to/icon.ico}} {{path/to/script.py}}`

- Include additional data files or directories in the bundle:

`pyinstaller --add-data "{{path/to/source}}:{{destination}}" {{path/to/script.py}}`

- Display help:

`pyinstaller {{[-h|--help]}}`

- Display version:

`pyinstaller {{[-v|--version]}}`
