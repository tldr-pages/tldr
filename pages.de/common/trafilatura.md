# trafilatura

> Ein Python-Tool zum Extrahieren und Crawlen von Webinhalten.
> Extrahiert Haupttext, Metadaten und Kommentare von Webseiten.
> Weitere Informationen: <https://trafilatura.readthedocs.io/en/latest/>.

- Extrahiere Text einer Website:

`trafilatura -u {{url}}`

- Extrahiere Text und speichere in einer Datei:

`trafilatura -u {{url}} -o {{pfad/zur/ausgabe.txt}}`

- Extrahiere Text im JSON-Format:

`trafilatura -u {{url}} --json-output`

- Extrahiere Text von mehreren URLs aus einer Datei:

`trafilatura --input-file {{pfad/zur/url_liste.txt}}`

- Crawle eine Website basierend auf einer Sitemap:

`trafilatura --sitemap {{url_zur_sitemap.xml}}`

- Extrahiere Text mit beibehaltener HTML-Formatierung:

`trafilatura -u {{url}} --formatting`

- Extrahiere Text inklusive Kommentare:

`trafilatura -u {{url}} --with-comments`

- Zeige Hilfe für weitere Optionen an:

`trafilatura --help`
