# http

> HTTPie: ein benutzerfreundliches HTTP-Tool.
> Weitere Informationen: <https://httpie.io/docs/cli/usage>.

- Sende eine GET-Anfrage (Zeigt ddie Header und den Body der Antwort):

`http {{https://example.com}}`

- Zeige nur den angegebenen Teil der Anfrage und der Antwort (`H`: Header der Anfrage, `B`: Body der Anfrage, `h`: Header der Antwort, `b`: Body der Antwort, `m`: Metadaten der Antwort):

`http {{[-p|--print]}} {{H|B|h|b|m|Hh|Hhb|...}} {{https://example.com}}`

- Spezifiziere die zu nutzende HTTP-Methode und nutze den angegebenen Proxy:

`http {{GET|POST|HEAD|PUT|PATCH|DELETE|...}} --proxy {{http|https}}:{{http://localhost:8080|socks5://localhost:9050|...}} {{https://example.com}}`

- Folge `3xx`-Umleitungen und spezifiziere zusätzliche Header für die Anfrage:

`http {{[-F|--follow]}} {{https://example.com}} {{'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'}}`

- Authentisiere gegenüber einem Server mithilfe unterschiedlicher Anthentisierungsmethoden:

`http {{[-a|--auth]}} {{username:password|token}} {{[-A|--auth-type]}} {{basic|digest|bearer}} {{GET|POST|...}} {{https://example.com/auth}}`

- Erstelle eine Anfrage ohne diese zu senden (ähnlich zu dry-run):

`http --offline {{GET|DELETE|...}} {{https://example.com}}`

- Nutze die angegebene Session für persistente benutzerdefinierte Header, Credentials für die Authentisierung und Cookies:

`http --session {{session_name|path/to/session.json}} {{[-a|--auth]}} {{username}}:{{password}} {{https://example.com/auth}} {{API-KEY:xxx}}`

- Lade eine Datei in ein Formular hoch (das folgende Beispiel geht davon aus, dass das Formularfeld als `<input type="file" name="cv" />` definiert ist):

`http {{[-f|--form]}} {{POST}} {{https://example.com/upload}} {{cv@path/to/file}}`
