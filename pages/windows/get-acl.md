# Get-Acl

> Get the security descriptor for a resource, such as a file or registry key.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>.

- Display the ACL for a specific directory:

`Get-Acl {{path\to\directory}}`

- Get an ACL for a registry key:

`Get-Acl -Path {{HKLM:\System\CurrentControlSet\Control}} | Format-List`
