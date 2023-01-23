# chrt

> Egy folyamat valós idejű attribútumainak manipulálása. További információ: <https://man7.org/linux/man-pages/man1/chrt.1.html>.

- Egy folyamat attribútumainak megjelenítése:

`chrt --pid {{PID}}`

- Egy folyamat összes szálának attribútumainak megjelenítése:

`chrt --all-tasks --pid {{PID}}`

- A `chrt` segítségével használható min/max prioritási értékek megjelenítése:

`chrt --max`

- Egy folyamat ütemezési politikájának beállítása:

`chrt --pid {{PID}} --{{deadline|idle|batch|rr|fifo|other}}`
