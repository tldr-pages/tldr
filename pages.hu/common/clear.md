# clear

> A terminál képernyőjének törlése. További információ: <https://manned.org/clear>.

- A képernyő törlése (a Control-L megnyomásával egyenértékű a Bash shellben):

`clear`

- Törli a képernyőt, de megtartja a terminál visszagörgetési pufferét:

`clear -x`

- Megadja a tisztítandó terminál típusát (alapértelmezés szerint a `TERM` környezeti változó értéke):

`clear -T {{type_of_terminal}}`

- A `ncurses` `clear` által használt verziójának megjelenítése:

`clear -V`
