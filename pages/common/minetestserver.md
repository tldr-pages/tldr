# minetestserver

> Multiplayer infinite-world block sandbox server.
> See also `minetest`, the graphical client.

- Start the server:

`minetestserver`

- List available worlds:

`minetestserver --world list`

- Specify the world name to load:

`minetestserver --world {{world_name}}`

- List the available game IDs:

`minetestserver --gameid list`

- Specify a game to use:

`minetestserver --gameid {{game_id}}`

- Listen on a specific port:

`minetestserver --port {{34567}}`

- Migrate to a different data backend:

`minetestserver --migrate {{sqlite3|leveldb|redis}}`

- Start an interactive terminal after starting the server:

`minetestserver --terminal`
