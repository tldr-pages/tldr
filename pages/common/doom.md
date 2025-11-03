# doom

> Classic open-source boomer shooter featuring modding and multiplayer.
> More information: <https://zdoom.org/wiki/Main_Page>.

- Start Doom:

`{{sourceport}}`

- Start with selected WAD:

`{{sourceport}} -iwad {{wad}}`

- Start with WAD and mods:

`{{sourceport}} -iwad {{wad}} -file {{pak3}} {{other mods}}`

- Start with auto-starting commands:

`{{sourceport}} -iwad {{wad}} +{{command}}`

- Host co-op multiplayer:

`{{sourceport}} -iwad {{wad}} +map {{map}} -host {{players}}`

- Host deathmatch multiplayer:

`{{sourceport}} -iwad {{wad}} +map {{map}} -host {{players}} -deathmatch`

- Join multiplayer:

`{{sourceport}} -iwad {{wad}} -join {{ip}}`
