# pyinstaller

> Bundle a Python application and its dependencies into a standalone executable.
> More information: <https://pyinstaller.org/en/stable/usage.html>.

- Build an executable from a Python script:

`pyinstaller {{path/to/script.py}}`

- Build a single-file executable:

`pyinstaller --onefile {{path/to/script.py}}`

- Build an executable without opening a console window:

`pyinstaller --windowed {{path/to/script.py}}`

- Build an executable with a custom name:

`pyinstaller --name {{application_name}} {{path/to/script.py}}`

- Build using an existing spec file:

`pyinstaller {{path/to/application.spec}}`
