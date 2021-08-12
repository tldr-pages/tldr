# wine

> Executați programele Windows pe Unix.
> Mai multe informaţii: <https://wiki.winehq.org/>

- Rulați programul `ipconfig.exe`:

`wine {{ipconfig}} {{/all}}`

- Rulați `cmd.exe` în fundal:

`wine start {{cmd}}`

- Executați Managerul de pachete ca Windows:

`wine uninstaller`

- Instalați pachete MSI:

`wine msiexec /i {{package}}`
