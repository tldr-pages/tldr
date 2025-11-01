# Doom source port

> Референс
> ZDoom wiki - Multiplayer: https://zdoom.org/wiki/Multiplayer

## Main tags
Если WAD в текущей папке и имеет стандартное название
```shell
<sourceport>
```
Если выбрать нужно WAD
```shell
<sourceport> -iwad <wad>
```
Моды
```shell
<sourceport> -iwad <wad> -file <pak3> <more mods can be included here>
```
Ну и дополнительные комманды по типу читов
```shell
<sourceport> -iwad <wad> +<your command here>
```
Мультиплеер:
```shell
<sourceport> -iwad <wad> <other parameters> +map <map> -host <number_of_players>
```
