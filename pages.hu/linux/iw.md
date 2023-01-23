# iw

> Vezeték nélküli eszközök megjelenítése és kezelése. További információ: <https://manned.org/iw>.

- Az elérhető vezeték nélküli hálózatok keresése:

`iw dev {{wlp}} scan`

- Csatlakozás egy nyitott vezeték nélküli hálózathoz:

`iw dev {{wlp}} connect {{SSID}}`

- Zárja le az aktuális kapcsolatot:

`iw dev {{wlp}} disconnect`

- Az aktuális kapcsolatra vonatkozó információk megjelenítése:

`iw dev {{wlp}} link`
