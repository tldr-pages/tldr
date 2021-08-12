# plantuml

> Creați diagrame UML dintr-un limbaj text simplu și le randați în diferite formate.
> Mai multe informaţii: <https://plantuml.com/en/command-line>

- Randare diagrame în format implicit (PNG):

`plantuml {{diagram1.puml}} {{diagram2.puml}}`

- Randați o diagramă în format dat (de exemplu, `png`, `pdf`, `svg`, `txt`):

`plantuml -t {{format}} {{diagram.puml}}`

- Randați toate diagramele unui director:

`plantuml {{path/to/diagrams}}`

- Randați o diagramă în directorul de ieșire:

`plantuml -o {{path/to/output}} {{diagram.puml}}`

- Randați o diagramă cu fișierul de configurare:

`plantuml -config {{config.cfg}} {{diagram.puml}}`

- Ajutor pentru afișare:

`plantuml -help`
