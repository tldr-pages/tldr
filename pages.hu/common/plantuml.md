# plantuml

> UML-diagramok készítése egyszerű szöveges nyelvből és különböző formátumokban történő megjelenítésük. További információ: <https://plantuml.com/en/command-line>.

- A diagramok alapértelmezett formátumban (PNG) történő megjelenítése:

`plantuml {{diagram1.puml}} {{diagram2.puml}}`

- Egy diagram adott formátumban történő megjelenítése (pl. `png`, `pdf`, `svg`, `txt`):

`plantuml -t {{format}} {{diagram.puml}}`

- Egy könyvtár összes diagramjának renderelése:

`plantuml {{path/to/diagrams}}`

- Egy diagram renderelése a kimeneti könyvtárba:

`plantuml -o {{path/to/output}} {{diagram.puml}}`

- Egy diagram renderelése a konfigurációs fájl segítségével:

`plantuml -config {{config.cfg}} {{diagram.puml}}`

- Súgó megjelenítése:

`plantuml -help`
