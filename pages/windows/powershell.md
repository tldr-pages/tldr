# powershell

> Command-line shell and scripting language designed especially for system administration.
> This command refers to PowerShell version 5.1 and below (also known as the legacy Windows PowerShell). To use the newer, cross-platform version of PowerShell (also known as PowerShell Core), use `pwsh` instead of `powershell`.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Start an interactive shell session:

`powershell`

- Start an interactive shell session without loading startup configs:

`powershell -NoProfile`

- Execute specific commands:

`powershell -Command "{{echo 'powershell is executed'}}"`

- Execute a specific script:

`powershell -File {{path/to/script.ps1}}`

- Start a session with a specific version of PowerShell:

`powershell -Version {{version}}`

- Prevent a shell from exit after running startup commands:

`powershell -NoExit`

- Describe the format of data sent to PowerShell:

`powershell -InputFormat {{Text|XML}}`

- Determine how an output from PowerShell is formatted:

`powershell -OutputFormat {{Text|XML}}`
