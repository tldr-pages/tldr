# Set-Acl

> Changes the security descriptor of a specified item, such as a file or a registry key.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-acl>.

- Copy a security descriptor from one file to another:

`$OriginAcl = Get-Acl -Path {{path\to\file}}; Set-Acl -Path {{path\to\file}} -AclObject $OriginAcl`

- Use the pipeline operator to pass a descriptor:

`Get-Acl -Path {{path\to\file}} | Set-Acl -Path {{path\to\file}}`
