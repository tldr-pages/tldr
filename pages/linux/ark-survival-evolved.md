# ARK: Survival Evolved

> Create and start a headless ARK: Survival Evolved server.
> More information: <https://ark.wiki.gg/wiki/Server_configuration>.

- Start the server with a specific map:

`{{path/to/ShooterGameServer}} {{TheIsland}}`

- Start the server with a specific session name, server password, and admin password:

`{{path/to/ShooterGameServer}} {{TheIsland}}?SessionName={{session_name}}?ServerPassword={{server_password}}?ServerAdminPassword={{admin_password}}`

- Start the server with a specific port and set a maximum player count:

`{{path/to/ShooterGameServer}} {{TheIsland}}?Port={{7777}}?MaxPlayers={{1..70}}`

- Enable PvE and disabling PvP:

`{{path/to/ShooterGameServer}} {{TheIsland}}?ServerPVE=true`

- Set a multiplier to scale the server difficulty, affecting the maximum level of wild creatures:

`{{path/to/ShooterGameServer}} {{TheIsland}}?DifficultyOffset={{1.0}}`

- Enable a specific event:

`{{path/to/ShooterGameServer}} {{TheIsland}} -ActiveEvent={{Summer}}`

- Enable automatic mod downloading, installation, and updating (Steam only):

`{{path/to/ShooterGameServer}} {{TheIsland}} -automanagedmods`

- Enable crossplay between Steam and EGS:

`{{path/to/ShooterGameServer}} {{TheIsland}} -crossplay -PublicIPForEpic={{ip_address}}`
