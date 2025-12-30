# wcurl

> Een eenvoudige wrapper rond `curl` om eenvoudig bestanden te downloaden.
> Zie ook: `wget`, `curl`.
> Meer informatie: <https://curl.se/wcurl/manual.html>.

- Download de inhoud van een URL naar een bestand dat wordt aangegeven door de URL ("index.html" in dit geval):

`wcurl {{https://example.com/index.html}}`

- Download de inhoud van een URL naar een bestand met een opgegeven naam:

`wcurl {{[-o|--output]}} {{pad/naar/bestand}} {{https://example.com/index.html}}`

- Download de inhoud van een URL, schakel de voortgangsbalk in en gebruik standaard HTTP/2:

`wcurl --curl-options "--progress-bar --http2" {{https://example.com/index.html}}`

- Hervat een onderbroken download:

`wcurl --curl-options "--clobber --continue-at -" {{https://example.com/index.html}}`
