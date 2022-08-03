# wine

> Run Windows executables on Unix-based systems.
> More information: <https://wiki.winehq.org/>.

- Run a specific program inside the `wine` environment:

`wine {{command}}`

- Run a specific program in background:

`wine start {{command}}`

- Install/uninstall an MSI package:

`wine msiexec /{{i|x}} {{path/to/package.msi}}`

- Run `File Explorer`, `Notepad`, or `WordPad`:

`wine {{explorer|notepad|write}}`

- Run `Registry Editor`, `Control Panel`, or `Task Manager`:

`wine {{regedit|control|taskmgr}}`

- Run the configuration tool:

`wine winecfg`
