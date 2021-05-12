# fish

> The Friendly Interactive SHell.
> Eine benutzerfreundliche Eingabeaufforderung.
> Weitere Informationen: <https://fishshell.com>.

- Starte eine interaktive Shell-Sitzung:

`fish`

- Führe einen Befehl aus:

`fish -c "{{befehl}}"`

- Führe ein Skript aus:

`fish {{pfad/zu/skript.fish}}`

- Überprüfe ein Skript auf Syntaxfehler:

`fish --no-execute {{pfad/zu/skript.fish}}`

- Starte eine private interaktive Shell-Sitzung, in der `fish` weder auf die Shell-History zugreift, noch diese verändert:

`fish --private`

- Gib die Version von fish aus:

`fish --version`

- Setze und exportiere eine permanente Umgebungsvariable (nur innerhalb der Shell):

`set -Ux {{variablenname}} {{variablenwert}}`
