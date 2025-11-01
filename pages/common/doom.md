# Doom source port

> Reference
> ZDoom wiki - Multiplayer: https://zdoom.org/wiki/Multiplayer

## Main tags
Just an wad
```shell
<sourceport>
```
If custom name
```shell
<sourceport> -iwad <wad>
```
And mods
```shell
<sourceport> -iwad <wad> -file <pak3> <more mods can be included here>
```
And you can add commands like
```shell
<sourceport> -iwad <wad> +<your command here>
```
To run doom multiplayer:
```shell
<sourceport> -iwad <wad> <other parameters> +map <map> -host <number_of_players>
```
