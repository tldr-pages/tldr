# chromium

> Open-source webbrowser voornamelijk ontwikkeld en onderhouden door Google.
> Meer informatie: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Open een specifieke URL of bestand:

`chromium {{https://example.com|pad/naar/bestand.html}}`

- Open in de incognito-modus:

`chromium --incognito {{example.com}}`

- Open in een nieuw venster:

`chromium --new-window {{example.com}}`

- Open in de applicatiemodus (zonder toolbars, URL-balk, knoppen, etc.):

`chromium --app={{https://example.com}}`

- Gebruik een proxyserver:

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- Open met een aangepaste profielmap:

`chromium --user-data-dir={{pad/naar/map}}`

- Open zonder CORS validatie (nuttig om een API te testen):

`chromium --user-data-dir={{pad/naar/map}} --disable-web-security`

- Open met een DevTools venster voor elk geopend tabblad:

`chromium --auto-open-devtools-for-tabs`
