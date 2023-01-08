# pwsh

> PowerShell Core is a cross-platform automation and configuration tool/framework.
> More information: <https://learn.microsoft.com/powershell/>.

- Start an instance of PowerShell:

`pwsh`

- Execute a script and then exit:

`pwsh -File {{path/to/file.ps1}}`

- Set the execution policy for the current session:

`pwsh -ExecutionPolicy {{AllSigned|Bypass|Default|RemoteSigned|Restricted|Undefined|Unrestricted}}`

- Execute a command and then exit:

`pwsh -Command {{command}}`
