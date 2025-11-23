# curl

> Zet gegevens over van of naar een server.
> Ondersteunt de meeste protocollen, waaronder HTTP, HTTPS, FTP, SCP, enz.
> Zie ook: `wget`.
> Meer informatie: <https://curl.se/docs/manpage.html>.

- Maak een HTTP GET-verzoek en dump de inhoud naar `stdout`:

`curl {{https://example.com}}`

- Maak een HTTP GET-verzoek, vo[L]g eventuele `3xx` redirects, en [D]ump de antwoordheaders en inhoud naar `stdout`:

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- Download een bestand en sla de [U]itvoer op onder de bestandsnaam zoals aangegeven door de URL:

`curl {{[-O|--remote-name]}} {{https://example.com/filename.zip}}`

- Stuur form-encoded [g]egevens (POST-verzoek van het type `application/x-www-form-urlencoded`). Gebruik `--data @file_name` of `--data @'-'` om van `stdin` te lezen:

`curl {{[-X|--request]}} POST {{[-d|--data]}} '{{name=bob}}' {{http://example.com/form}}`

- Stuur een verzoek met een extra header, met behulp van een aangepaste HTTP-methode en via een pro[x]y (zoals BurpSuite), waarbij onveilige zelfondertekende certificaten worden genegeerd:

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} '{{Authorization: Bearer token}}' {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Verstuur gegevens in JSON-formaat, met de juiste Content-Type [H]eader:

`curl {{[-d|--data]}} '{{{"name":"bob"}}}' {{[-H|--header]}} '{{Content-Type: application/json}}' {{http://example.com/users/1234}}`

- Verstrek een clientcertificaat en privésleutel voor het verzoek, en sla de certificaatvalidatie over:

`curl {{[-E|--cert]}} {{client.pem}} --key {{key.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- Los een hostnaam op naar een aangepast IP-adres, met [v]erbose uitvoer (vergelijkbaar met het bewerken van het `/etc/hosts`-bestand voor aangepaste DNS-resolutie):

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
