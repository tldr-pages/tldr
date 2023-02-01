# pwsh

> PowerShell Core is a cross-platform automation and configuration tool/framework.
> See also: `powershell`.
> More information: <https://learn.microsoft.com/powershell/>.

- Start an interactive shell session:

`pwsh`

- Start an interactive shell session without loading startup configs:

`pwsh -NoProfile`

- Execute specific commands:

`pwsh -Command "{{string}}"`

- Execute a specific script:

`pwsh {{path/to/script.ps1}}`

- Start an interactive shell session with a specific execution policy:

`pwsh -ExecutionPolicy {{AllSigned|Bypass|Default|RemoteSigned|Restricted|...}}`
