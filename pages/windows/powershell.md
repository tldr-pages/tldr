# powershell

> Command-line shell and scripting language designed especially for system administration.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Start an interactive shell session:

`powershell`

- Start an interactive shell session without loading startup configs:

`powershell -NoProfile`

- Execute a command:

`powershell -Command "{{command}}"`

- Execute a script:

`powershell -File {{path/to/script.ps1}}`

- Start a session with a specified version of PowerShell:

`powershell -Version {{version}}`

- Prevent the shell from exit after running startup commands:

`powershell -NoExit`

- Describe the format of data sent to PowerShell:

`powershell -InputFormat {{Text|XML}}`

- Determine how output from PowerShell is formatted:

`powershell -OutputFormat {{Text|XML}}`
