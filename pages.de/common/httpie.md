# HTTPie

> Ein benutzerfreundliches HTTP-Tool.
> Weitere Informationen: <https://github.com/httpie/httpie>.

- Sende eine GET-Anfrage (Standardmethode ohne Anfragedaten):

`http {{https://example.com}}`

- Sende eine POST-Anfrage (Standardmethode mit Anfragedaten):

`http {{https://example.com}} {{hello=World}}`

- Sende eine POST-Anfrage mit einer Datei als Eingabe:

`http {{https://example.com}} < {{file.json}}`

- Sende eine PUT-Anfrage mit einem bestimmten JSON-Body:

`http PUT {{https://example.com/todos/7}} {{hello=world}}`

- Sende eine DELETE-Anfrage mit einem bestimmten Anfrage-Header:

`http DELETE {{https://example.com/todos/7}} {{API-Key:foo}}`

- Zeige den gesamten HTTP-Austausch (sowohl Anfrage als auch Antwort):

`http -v {{https://example.com}}`

- Lade eine Datei herunter:

`http --download {{https://example.com}}`

- Folge Umleitungen und zeige Zwischenanfragen und -antworten:

`http --follow --all {{https://example.com}}`
