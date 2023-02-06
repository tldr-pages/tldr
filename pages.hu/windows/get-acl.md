# Get-Acl

> Egy erőforrás, például egy fájl vagy egy beállításkulcs biztonsági leírójának lekérdezése. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>.

- Egy adott könyvtár ACL-jének megjelenítése:

`Get-Acl {{path/to/directory}}`

- Egy beállításkulcs ACL-jének lekérdezése:

`Get-Acl -Path {{HKLM:\System\CurrentControlSet\Control}} | Format-List`
