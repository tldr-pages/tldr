# wmctrl

> CLI for X Window Manager. További információ: <https://manned.org/wmctrl>.

- Az ablakkezelő által kezelt összes ablak listázása:

`wmctrl -l`

- Váltson az első olyan ablakra, amelynek (részleges) címe megegyezik:

`wmctrl -a {{window_title}}`

- Egy ablak áthelyezése az aktuális munkaterületre, felemelése és fókuszba helyezése:

`wmctrl -R {{window_title}}`

- Váltás egy munkaterületre:

`wmctrl -s {{workspace_number}}`

- Egy ablak kiválasztása és a teljes képernyő bekapcsolása:

`wmctrl -r {{window_title}} -b toggle,fullscreen`

- Egy ablak kiválasztása és áthelyezése egy munkaterületre:

`wmctrl -r {{window_title}} -t {{workspace_number}}`
