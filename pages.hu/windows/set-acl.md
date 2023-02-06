# Set-Acl

> Egy megadott elem, például egy fájl vagy egy beállításkulcs biztonsági leírójának módosítása. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-acl>.

- Biztonsági leíró másolása egyik fájlból egy másikba:

`$OriginAcl = Get-Acl -Path {{path/to/file}}; Set-Acl -Path {{path/to/file}} -AclObject $OriginAcl`

- A csővezeték-operátor használatával átadhat egy leírót:

`Get-Acl -Path {{path/to/file}} | Set-Acl -Path {{path/to/file}}`
