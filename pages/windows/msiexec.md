# msiexec

> Install, update, repair, or uninstall Windows programs through MSI and MSP apckage files.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec>.

- Install a program from its MSI package:

`msiexec /package {{path/to/file.msi}}`

- Install a MSI package from a website:

`msiexec /package {{https://example.com/installer.msi}}`

- Install a MSP patch file:

`msiexec /update {{path/to/file.msp}}`

- Uninstall a program or patch using their respective MSI or MSP file:

`msiexec /uninstall {{path/to/file}}`
