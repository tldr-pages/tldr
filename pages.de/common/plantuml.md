# plantuml

> Erstelle UML-Diagramme aus einer reinen Textsprache und rendere sie in verschiedenen Formaten.
> Weitere Informationen: <https://plantuml.com/en/command-line>.

- Rendere Diagramme im Standardformat (PNG):

`plantuml {{pfad/zu/diagramm1.puml}} {{pfad/zu/diagramm2.puml}}`

- Rendere ein Diagramm im vorgegebenen Format (z.B. `png`, `pdf`, `svg`, `txt`):

`plantuml -t {{format}} {{pfad/zu/diagramm.puml}}`

- Rendere alle Diagramme eines Verzeichnisses:

`plantuml {{pfad/zu/verzeichnis}}`

- Rendere ein Diagramm in ein bestimmtes Ausgabeverzeichnis:

`plantuml -o {{pfad/zu/verzeichnis}} {{pfad/zu/diagramm.puml}}`

- Rendere ein Diagramm mit einer bestimmten Konfigurationsdatei:

`plantuml -config {{pfad/zu/konfig.cfg}} {{pfad/zu/diagramm.puml}}`

- Zeige Hilfe an:

`plantuml -help`
