# doom

> Классический шутер с открытым исходным кодом, ориентированный на моддинг и многопользовательский режим.
> Больше информации: <https://doomwiki.org/wiki/Source_port_parameters>.

- Запустить Doom:

`{{sourceport}}`

- Запустить с выбранным WAD:

`{{sourceport}} -iwad {{wad}}`

- Запустить с WAD и модами:

`{{sourceport}} -iwad {{wad}} -file {{pak3}} {{other mods}}`

- Запустить с автостартовыми командами:

`{{sourceport}} -iwad {{wad}} +{{command}}`

- Запустить кооперативный многопользовательский режим:

`{{sourceport}} -iwad {{wad}} +map {{map}} -host {{players}}`

- Запустить многопользовательский режим "deathmatch":

`{{sourceport}} -iwad {{wad}} +map {{map}} -host {{players}} -deathmatch`

- Присоединиться к многопользовательской игре:

`{{sourceport}} -iwad {{wad}} -join {{ip}}`
