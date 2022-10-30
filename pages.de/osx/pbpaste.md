# pbpaste

> Sende den Inhalt der Zwischenablage zum Standardoutput.
> Weitere Informationen: <https://ss64.com/osx/pbpaste.html>.

- Schreibe den Inhalt der Zwischenablage in eine Datei:

`pbpaste > {{datei}}`

- Speichere die Zwischenablage in einer Datei im Benutzerverzwichnis an:

`pbpaste > ~/{{datei}}`

- Benutze die Zwischenablage als Eingabe für andere Kommandos:

`pbpaste | grep foo`

`pbpaste | base64 | pbcopy`