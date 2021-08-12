# minetestserver

> Multiplayer infinit lume bloc sandbox server.
> A se vedea, de asemenea, `minetest`, clientul grafic.
> Mai multe informaţii: <https://wiki.minetest.net/Setting_up_a_server>

- Porniţi serverul:

`minetestserver`

- Lista lumilor disponibile:

`minetestserver --world list`

- Specificați numele lumii pentru a încărca:

`minetestserver --world {{world_name}}`

- Listează ID-uri de joc disponibile:

`minetestserver --gameid list`

- Specificați un joc de utilizat:

`minetestserver --gameid {{game_id}}`

- Ascultați pe un anumit port:

`minetestserver --port {{34567}}`

- Migrarea la un alt backend de date:

`minetestserver --migrate {{sqlite3|leveldb|redis}}`

- Porniți un terminal interactiv după pornirea serverului:

`minetestserver --terminal`
