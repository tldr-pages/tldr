# Get-Acl

> Gets the security descriptor for a resource, such as a file or registry key.
> This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-acl>.

- Get an ACL for a folder:

`Get-Acl C:\Windows`

- Get an ACL for a registry key:

`Get-Acl -Path {{HKLM:\System\CurrentControlSet\Control}} | Format-List`
