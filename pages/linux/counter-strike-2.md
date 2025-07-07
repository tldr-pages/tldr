# counter strike 2

> Host a headless Counter Strike 2 server.
> More information: <https://developer.valvesoftware.com/wiki/Counter-Strike_2/Dedicated_Servers>.

- Run a game with one map:

`{{path/to/cs2}} -dedicated +map {{de_dust2}}`

- Run a game with specified maximum number of players:

`{{path/to/cs2}}  -dedicated +map {{de_dust2}} -maxplayers {{64}}`

- Run a game with specified server IP and port:

`{{path/to/cs2}} -dedicated +map {{de_dust2}} -ip {{1.2.3.4}} -port {{27015}}`

- Shut the server down:

`quit`
