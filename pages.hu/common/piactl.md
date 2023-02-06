# piactl

> A Private Internet Access, egy kereskedelmi VPN szolgáltató parancssori eszköze. További információ: <https://helpdesk.privateinternetaccess.com/kb/articles/pia-desktop-command-line-interface-part-1>.

- Jelentkezzen be a Private Internet Access szolgáltatásba:

`piactl login {{path/to/login_file}}`

- Csatlakozás a Private Internet Access szolgáltatáshoz:

`piactl connect`

- Lekapcsolódás a Private Internet Accessről:

`piactl disconnect`

- A Private Internet Access démon engedélyezése vagy letiltása a háttérben:

`piactl background {{enable|disable}}`

- Az összes elérhető VPN-régió listázása:

`piactl get regions`

- Az aktuális VPN-régió megjelenítése:

`piactl get region`

- A VPN-régió beállítása:

`piactl set region {{region}}`

- Kijelentkezés a Private Internet Accessből:

`piactl logout`
