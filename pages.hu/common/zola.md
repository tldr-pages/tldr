# zola

> Statikus webhelygenerátor egyetlen binárisban, minden beépített elemmel. További információ: <https://www.getzola.org/documentation/getting-started/cli-usage/>.

- A Zola által használt könyvtárstruktúra létrehozása a megadott könyvtárban:

`zola init {{my_site}}`

- Építse fel a teljes webhelyet a `public` könyvtárban, miután törölte azt:

`zola build`

- Építse a teljes webhelyet egy másik könyvtárba:

`zola build --output-dir {{path/to/output_directory/}}`

- Építse fel és szolgálja ki a webhelyet egy helyi szerver segítségével (alapértelmezett a `127.0.0.1:1111`):

`zola serve`

- Az összes oldalt ugyanúgy építi fel, mint a build parancs, de anélkül, hogy az eredményeket a lemezre írná:

`zola check`
