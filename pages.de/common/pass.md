# pass

> Programm zum Speichern und Lesen von Passwörtern und anderen sensiblen Daten.
> Die Daten sind mit GPG verschlüsselt und werden mit einem Git repository verwaltet.
> Weitere Informationen: <https://www.passwordstore.org>.

- Initialisiere oder verschlüssle einen neuen oder bestehenden Speicher mit einer oder mehreren GPG IDs neu:

`pass init {{gpg_id_1}} {{gpg_id_2}}`

- Speichere das Passwort und zusätzliche Informationen (Str + D auf neuer Zeile zum abschließen):

`pass insert --multiline {{pfad/zu/datei}}`

- Bearbeite einen bestimmten Eintrag:

`pass edit {{pfad/zu/datei}}`

- Kopiere das Passwort (die erste Zeile des Eintrags) in die Zwischenablage:

`pass -c {{pfad/zu/datei}}`

- Zeige die Baumstruktur des Passwort-Stores an:

`pass`

- Generiere ein neues, zufälliges Passwort mit Länge n und kopiere is in die Zwischenablage:

`pass generate -c {{pfad/zu/datei}} {{n}}`

- Initialisiere ein Git Repository (Alle durch pass durchgeführten Änderungen werden automatisch committed):

`pass git init`

- Führe einen Git-Befehl für den Passwort-Store aus:

`pass git {{befehl}}`
