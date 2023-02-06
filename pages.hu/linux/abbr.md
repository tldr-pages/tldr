# abbr

> A halhéj rövidítések kezelése. A felhasználó által meghatározott szavak beírása után hosszabb kifejezésekre cserélődnek. További információ: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Új rövidítés hozzáadása:

`abbr --add {{abbreviation_name}} {{command}} {{command_arguments}}`

- Meglévő rövidítés átnevezése:

`abbr --rename {{old_name}} {{new_name}}`

- Meglévő rövidítés törlése:

`abbr --erase {{abbreviation_name}}`

- Egy másik állomáson definiált rövidítések importálása SSH-n keresztül:

`ssh {{host_name}} abbr --show | source`
