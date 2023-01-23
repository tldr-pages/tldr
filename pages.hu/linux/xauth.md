# xauth

> Az X-kiszolgálóhoz való csatlakozáshoz használt engedélyezési információk szerkesztése és megjelenítése. További információ: <https://manned.org/xauth>.

- Interaktív üzemmód indítása egy adott jogosultsági fájllal (alapértelmezett: `~/.Xauthority`):

`xauth -f {{path/to/file}}`

- A hatósági fájlra vonatkozó információk megjelenítése:

`xauth info`

- Az összes megjelenítésre vonatkozó jogosultsági bejegyzés megjelenítése:

`xauth list`

- Engedélyezés hozzáadása egy adott kijelzőhöz:

`xauth add {{display_name}} {{protocol_name}} {{key}}`

- Engedélyezés eltávolítása egy adott kijelzőhöz:

`xauth remove {{display_name}}`

- Az aktuális kijelző engedélyezési bejegyzésének kiírása az stdoutra:

`xauth extract - $DISPLAY`

- Egy adott fájlból származó engedélyezési bejegyzések egyesítése az engedélyezési adatbázisba:

`cat {{path/to/file}} | xauth merge -`

- Súgó megjelenítése:

`xauth --help`
