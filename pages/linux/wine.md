# wine

> Run Windows programs on Unix.
> More information: <https://wiki.winehq.org/>.

- Run a specific program:

`wine {{command}}`

- Run a specific program in a background:

`wine start {{command}}`

- Install/uninstall an MSI package:

`wine msiexec /{{i|x}} {{path/to/package.msi}}`

- Run `File Explorer`/`Notepad`/`WordPad`:

`wine {{explorer|notepad|write}}`

- Run `Registry Editor`/`Control Panel`/`Task Manager`:

`wine {{regedit|control|taskmgr}}`

- Run configuration tool:

`wine winecfg`
