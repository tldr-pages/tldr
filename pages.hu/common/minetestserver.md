# minetestserver

> Multiplayer infinite-world block sandbox szerver. Lásd még: `minetest`, a grafikus kliens. További információ: <https://wiki.minetest.net/Setting_up_a_server>.

- Indítsa el a szervert:

`minetestserver`

- Az elérhető világok listája:

`minetestserver --world list`

- Adja meg a betöltendő világ nevét:

`minetestserver --world {{world_name}}`

- Az elérhető játékazonosítók listázása:

`minetestserver --gameid list`

- A használni kívánt játék megadása:

`minetestserver --gameid {{game_id}}`

- Figyeljen egy adott porton:

`minetestserver --port {{34567}}`

- Másik adatbázishoz való áttérés:

`minetestserver --migrate {{sqlite3|leveldb|redis}}`

- Interaktív terminál indítása a szerver indítása után:

`minetestserver --terminal`
