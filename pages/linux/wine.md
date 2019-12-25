# wine

> Run Windows programs on Unix.
> More information: <https://wiki.winehq.org/>.

- Run ipconfig.exe program:

`wine {{ipconfig}} {{/all}}`

- Run cmd.exe in background:

`wine start {{cmd}}`

- Run Windows-like Package Manager:

`wine uninstaller`

- Install MSI packages:

`wine msiexec /i {{package}}`
