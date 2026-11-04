# firefox

> Een gratis en open source webbrowser.
> Meer informatie: <https://wiki.mozilla.org/Firefox/CommandLineOptions>.

- Start Firefox en open een webpagina:

`firefox {{https://www.duckduckgo.com}}`

- Open een nieuw venster:

`firefox --new-window {{https://www.duckduckgo.com}}`

- Open een privévenster (incognito):

`firefox --private-window`

- Zoek naar "wikipedia" met de standaard zoekmachine:

`firefox --search "{{wikipedia}}"`

- Start Firefox in veilige modus, met alle extensies uitgeschakeld:

`firefox --safe-mode`

- Maak een screenshot van een webpagina in headless modus:

`firefox --headless --screenshot {{pad/naar/uitvoerbestand.png}} {{https://example.com/}}`

- Gebruik een specifiek profiel om meerdere aparte instanties van Firefox tegelijk te laten draaien:

`firefox --profile {{pad/naar/map}} {{https://example.com/}}`

- Stel Firefox in als standaardbrowser:

`firefox --setDefaultBrowser`
