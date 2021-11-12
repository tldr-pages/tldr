# pwsh

> PowerShell Core is a cross-platform automation and configuration tool/framework.
> More information: <https://docs.microsoft.com/powershell/>.

- Start an interactive shell session:

`pwsh`

- Start an interactive shell session without loading startup configs:

`pwsh -nop`

- Execute a [c]ommand:

`pwsh -c "{{command}}"`

- Execute a script:

`pwsh {{path/to/script.ps1}}`

- Start an interactive shell session with specified [e]xecution [p]olicy:

`pwsh -ep {{AllSigned|Bypass|Default|RemoteSigned|Restricted|Undefined|Unrestricted}}`

- Print the [v]ersion:

`pwsh -v`
