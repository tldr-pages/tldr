# sqlite3

> Das Kommandozeileninterface für SQLite 3, welches eine eigenständige dateibasierte eingebettete SQL-Engine ist.
> Weitere Informationen: <https://sqlite.org>.

- Starte eine interaktive Shell mit einer neuen Datenbank:

`sqlite3`

- Öffne eine interaktive Shell mit einer existierenden Datenbank:

`sqlite3 {{pfad/zu/datenbank.sqlite3}}`

- Führe ein SQL Statement auf einer existierenden Datenbank aus und beende die Ausführung danach:

`sqlite3 {{pfad/zu/datenbank.sqlite3}} '{{SELECT * FROM einer_tabelle;}}'`
