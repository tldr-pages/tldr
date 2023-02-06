# logoff

> Bejelentkezési munkamenet befejezése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>.

- Az aktuális munkamenet befejezése:

`logoff`

- A munkamenet megszüntetése a neve vagy az azonosítója alapján:

`logoff {{session_name|session_id}}`

- RDP-n keresztül csatlakoztatott munkamenet megszüntetése egy adott kiszolgálón:

`logoff {{session_name|session_id}} /server:{{servername}}`
