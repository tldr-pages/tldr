# trafilatura

> Ein Python-Tool zum Extrahieren und Crawlen von Webinhalten.
> Extrahiert Haupttext, Metadaten und Kommentare von Webseiten.
> Weitere Informationen: <https://trafilatura.readthedocs.io/en/latest/usage-cli.html#further-information>.

- Extrahiere Text einer Website:

`trafilatura {{[-u|--URL]}} {{url}}`

- Extrahiere Text und speichere diesen in einer Datei:

`trafilatura {{[-u|--URL]}} {{url}} {{[-o|--output-dir]}} {{pfad/zur/ausgabe.txt}}`

- Extrahiere Text im JSON-Format:

`trafilatura {{[-u|--URL]}} {{url}} --json`

- Extrahiere Text von mehreren URLs aus einer Datei:

`trafilatura {{[-i|--input-file]}} {{pfad/zur/url_liste.txt}}`

- Crawle eine Website basierend auf einer Sitemap:

`trafilatura --sitemap {{url_zur_sitemap.xml}}`

- Extrahiere Text unter Beibehaltung der HTML-Formatierung:

`trafilatura {{[-u|--URL]}} {{url}} --formatting`

- Extrahiere Text inklusive Kommentare:

`trafilatura {{[-u|--URL]}} {{url}} --with-comments`

- Zeige Hilfe an:

`trafilatura {{[-h|--help]}}`
