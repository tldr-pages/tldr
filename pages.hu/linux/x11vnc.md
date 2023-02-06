# x11vnc

> Egy VNC-kiszolgáló, amely lehetővé teszi a VNC-t egy meglévő megjelenítő szerveren. Alapértelmezés szerint a kiszolgáló automatikusan megszűnik, amint az összes kliens leválik róla. További információ: <https://manned.org/x11vnc>.

- Olyan VNC-kiszolgáló indítása, amely lehetővé teszi több ügyfél csatlakoztatását:

`x11vnc -shared`

- Olyan VNC-kiszolgáló indítása, amely csak megtekintési módban működik, és amely nem szűnik meg, ha az utolsó ügyfél megszakítja a kapcsolatot:

`x11vnc -forever -viewonly`

- VNC-kiszolgáló indítása egy adott kijelzőn és képernyőn (mindkettő a nulladik indexen kezdődik):

`x11vnc -display :{{display}}.{{screen}}`

- VNC-kiszolgáló indítása a harmadik kijelző alapértelmezett képernyőjén:

`x11vnc -display :{{2}}`

- VNC-kiszolgáló indítása az első kijelző második képernyőjén:

`x11vnc -display :{{0}}.{{1}}`
