# fish

> The Friendly Interactive SHell.
> Eine benutzerfreundliche Eingabeaufforderung.
> Mehr Informationen: <https://fishshell.com>.

- Starte interaktive Eingabeaufforderung:

`fish`

- Führe einen Befehl aus:

`fish -c "{{befehl}}"`

- Führe Befehle von Datei aus:

`fish {{datei.fish}}`

- Überprüfe eine Datei auf Syntax Fehler:

`fish --no-execute {{datei.fish}}`

- Zeige Informationen über derzeitige Version und schließe:

`fish --version`

- Setze und exportiere Umgebungsvariabeln die nach einem Neustart weiter bestehen:

`set -Ux {{variable_name}} {{variable_wert}}`
