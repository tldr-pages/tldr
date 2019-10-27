# wine

> Run Windows programs on Unix.
> More information: <https://wiki.winehq.org/>.

- Run a program with args:

`wine {{program}} {{program args}}`

- Run a program with args in background:

`wine start {{program}} {{program args}}`

- Run Windows-like Package Manager:

`wine uninstaller`

- Install MSI packages:

`wine msiexec /i {{package}}`
