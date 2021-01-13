# plantuml

> Erstellen Sie UML-Diagramme aus einer reinen Textsprache und rendern Sie sie in verschiedenen Formaten.
> Mehr Informationen: <https://plantuml.com/en/command-line>.

- Rendern von Diagrammen im Standardformat (PNG):

`plantuml {{diagramm1.puml}} {{diagramm2.puml}}`

- Rendern eines Diagramms im vorgegebenen Format (z.B. `png`, `pdf`, `svg`, `txt`):

`plantuml -t {{Format}} {{diagram.puml}}`

- Rendern Sie alle Diagramme eines Verzeichnisses:

`plantuml {{Pfad/der/Diagramme}}`

- Rendern Sie ein Diagramm in das Ausgabeverzeichnis:

`plantuml -o {{Pfad/zur/Ausgabe}} {{diagramm.puml}}`

- Rendern Sie ein Diagramm mit der Konfigurationsdatei:

`plantuml -config {{konfig.cfg}} {{diagramm.puml}}`

- Hilfe anzeigen:

`plantuml -help`
