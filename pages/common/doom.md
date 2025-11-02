# doom

> Open source classic boomer shooter with modding and multiplayer.
> More information: <https://zdoom.org/wiki/Multiplayer>

- Start doom:

`<sourceport>`

- Start with selected wad:

`<sourceport> -iwad <wad>`

- Start with wad and mods:

`<sourceport> -iwad <wad> -file <pak3> <more mods can be included here>`

- Start with auto-starting commands:

`<sourceport> -iwad <wad> +<your command here>`

- Host co-op multiplayer:

`<sourceport> -iwad <wad> <other parameters> +map <map> -host <number_of_players>`

- Host deathmatch multiplayer:

`<sourceport> -iwad <wad> <othere parameters> +map <map> -host <number_of_players> -deathmatch`

- Join multiplayer:

`<sourceport> -iwad <wad> <other parameters> -join <ip>`

- Play demo:

`<sourceport> -iwad <wad> -playdemo <demofile>.lmp`

- Record demo:

`<sourceport> -iwad <wad> -record <demofile>.lmp`
