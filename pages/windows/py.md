# py

> Python Launcher for Windows that runs with specified Python version.
> See also: `python`.
> More information: <https://docs.python.org/using/windows.html#python-launcher-for-windows>.

- Start a REPL (interactive shell), optionally with arguments supported by `python` (like `-c`, `-m`, etc.):

`py {{python_arguments}}`

- Execute a specific Python file:

`py {{path/to/file.py}}`

- Run specific Python version. If the version is missing, and `PYLAUNCHER_ALLOW_INSTALL` environment variable is set, auto-install via Microsoft Store or Winget:

`py {{-2|-3.7|...}}`

- List installed Python versions:

`py --list`
