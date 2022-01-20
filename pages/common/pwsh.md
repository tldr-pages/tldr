# pwsh

> PowerShell Core is a cross-platform automation and configuration tool/framework.
> More information: <https://docs.microsoft.com/powershell/>.

- Start an interactive shell session:

`pwsh`

- Start an interactive shell session without loading startup configs:

`pwsh -NoProfile`

- Execute commands:

`pwsh -Command "{{echo 'pwsh is executed'}}"`

- Execute a script:

`pwsh {{path/to/script.ps1}}`

- Start an interactive shell session with a specified execution policy:

`pwsh -ExecutionPolicy {{AllSigned|Bypass|Default|RemoteSigned|Restricted|Undefined|Unrestricted}}`
