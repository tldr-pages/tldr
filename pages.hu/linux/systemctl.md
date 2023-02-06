# systemctl

> A systemd rendszer- és szolgáltatáskezelő vezérlése. További információ: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Az összes futó szolgáltatás megjelenítése:

`systemctl status`

- A meghibásodott egységek listázása:

`systemctl --failed`

- Egy szolgáltatás indítása/leállítása/újraindítása/visszaállítása:

`systemctl {{start|stop|restart|reload}} {{unit}}`

- Egy egység állapotának megjelenítése:

`systemctl status {{unit}}`

- Engedélyezze/tiltja egy egység indítását a rendszerindításkor:

`systemctl {{enable|disable}} {{unit}}`

- Egység maszkolása/lenyomása az engedélyezés és a kézi aktiválás megakadályozása érdekében:

`systemctl {{mask|unmask}} {{unit}}`

- A systemd újratöltése, új vagy megváltozott egységek keresése:

`systemctl daemon-reload`

- Ellenőrizze, hogy egy egység engedélyezve van-e:

`systemctl is-enabled {{unit}}`
