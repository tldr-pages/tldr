# pass

> Programm zum speichern und lesen von Passwörtern und anderen empfindlichen Daten.
> Die Daten sind mit GPG verschlüsselt und mit einem Git repository verwaltet.
> Mehr Informationen: <https://www.passwordstore.org>.

- Neuen oder bestehenden Speicher mit einer oder mehreren GPG IDs initialisieren oder neu verschlüsseln:

`pass init {{gpg_id_1}} {{gpg_id_2}}`

- Passwort und zusätzliche Informationen speichern (Str + D auf neuer Zeile zum abschließen):

`pass insert --multiline {{pfad/zu/daten}}`

- Einen Eintrag bearbeiten:

`pass edit {{pfad/zu/daten}}`

- Passwort (Erste Zeile des Eintrags) in die Zwischenablage kopieren:

`pass -c {{pfad/zu/daten}}`

- Tree des Passwort stores anzeigen:

`pass`

- Neues, zufälliges Passwort mit Länge n generieren und in die Zwischenablage kopieren:

`pass generate -c {{pfad/zu/daten}} {{n}}`

- Neues Git Repository initialisieren (Alle durch pass durchgeführten änderungen werden automatisch committed):

`pass git init`
