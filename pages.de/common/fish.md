# fish

> The Friendly Interactive SHell.
> Eine benutzerfreundliche Eingabeaufforderung.
> Weitere Informationen: <https://fishshell.com>.

- Starte eine interaktive Shell-Sitzung:

`fish`

- Starte eine interaktive Shell-Sitzung ohne die Start-Konfiguration zu laden:

`fish --no-config`

- Führe einen bestimmten Befehl aus:

`fish --command "{{echo 'fish wird ausgeführt'}}"`

- Führe ein bestimmtes Skript aus:

`fish {{pfad/zu/skript.fish}}`

- Überprüfe ein bestimmtes Skript auf Syntaxfehler:

`fish --no-execute {{pfad/zu/skript.fish}}`

- Starte eine private, interaktive Shell-Sitzung, in der `fish` weder auf die Shell-History zugreift, noch diese verändert:

`fish --private`

- Definiere und exportiere eine Umgebungsvariable, die über mehrere Shell-Neustarts hinweg existiert (builtin):

`set --universal --export {{variablenname}} {{variablenwert}}`
