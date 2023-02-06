# powershell

> Kifejezetten rendszergazdai feladatokhoz tervezett parancssori héj és szkriptnyelv. Lásd még: `pwsh`. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Interaktív shell munkamenet indítása:

`powershell`

- Interaktív shell munkamenet indítása az indítási konfigurációk betöltése nélkül:

`powershell -NoProfile`

- Konkrét parancsok végrehajtása:

`powershell -Command "{{echo 'powershell is executed'}}"`

- Egy adott szkript végrehajtása:

`powershell -File {{path/to/script.ps1}}`

- Munkamenet indítása a PowerShell egy adott verziójával:

`powershell -Version {{version}}`

- A héj kilépésének megakadályozása az indítási parancsok futtatása után:

`powershell -NoExit`

- A PowerShellnek küldött adatok formátumának leírása:

`powershell -InputFormat {{Text|XML}}`

- A PowerShell kimeneteinek formázásának meghatározása:

`powershell -OutputFormat {{Text|XML}}`
