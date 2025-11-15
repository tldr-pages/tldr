# http

> HTTPie: een HTTP-client ontworpen voor het testen, debuggen en in het algemeen interactie met API's en HTTP-servers.
> Meer informatie: <https://httpie.io/docs/cli/usage>.

- Maak een eenvoudige GET-aanvraag (toont response header en inhoud):

`http {{https://example.org}}`

- Print specifieke uitvoerinhoud (`H`: request headers, `B`: request body, `h`: response headers, `b`: response body, `m`: response metadata):

`http {{[-p|--print]}} {{H|B|h|b|m|Hh|Hhb|...}} {{https://example.com}}`

- Specificeer de HTTP-methode bij het verzenden van een aanvraag en gebruik een proxy om de aanvraag te onderscheppen:

`http {{GET|POST|HEAD|PUT|PATCH|DELETE|...}} --proxy {{http|https}}:{{http://localhost:8080|socks5://localhost:9050|...}} {{https://example.com}}`

- Volg eventuele `3xx` redirects en specificeer extra headers in een verzoek:

`http {{[-F|--follow]}} {{https://example.com}} {{'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'}}`

- Authenticeer bij een server met verschillende authenticatiemethoden:

`http {{[-a|--auth]}} {{gebruikersnaam:wachtwoord|token}} {{[-A|--auth-type]}} {{basic|digest|bearer}} {{GET|POST|...}} {{https://example.com/auth}}`

- Maak een verzoek maar verzend het niet (vergelijkbaar met een dry-run):

`http --offline {{GET|DELETE|...}} {{https://example.com}}`

- Gebruik benoemde sessies voor aanhoudende aangepaste headers, auth-referenties en cookies:

`http --session {{session_naam|pad/naar/session.json}} {{[-a|--auth]}} {{gebruikersnaam}}:{{wachtwoord}} {{https://example.com/auth}} {{API-KEY:xxx}}`

- Upload een bestand naar een formulier (het onderstaande voorbeeld gaat ervan uit dat het formulier `<input type="file" name="cv" />` is):

`http {{[-f|--form]}} {{POST}} {{https://example.com/upload}} {{cv@pad/naar/bestand}}`
