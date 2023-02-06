# pwsh

> A PowerShell Core egy platformokon átívelő automatizálási és konfigurációs eszköz/keretrendszer. További információ: <https://learn.microsoft.com/powershell/>.

- Indítsa el a PowerShell egy példányát:

`pwsh`

- Végezzen el egy szkriptet, majd lépjen ki:

`pwsh -File {{path/to/file.ps1}}`

- Az aktuális munkamenet végrehajtási házirendjének beállítása:

`pwsh -ExecutionPolicy {{AllSigned|Bypass|Default|RemoteSigned|Restricted|Undefined|Unrestricted}}`

- Egy parancs végrehajtása, majd kilépés:

`pwsh -Command {{command}}`
