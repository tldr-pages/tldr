# svgo

> SVG Optimizer: Node.js alapú eszköz a skálázható vektorgrafikus fájlok optimalizálására. Egy sor transzformációs szabályt (plugint) alkalmaz, amelyek egyenként kapcsolhatók. További információ: <https://github.com/svg/svgo>.

- Egy fájl optimalizálása az alapértelmezett bővítmények használatával (felülírja az eredeti fájlt):

`svgo {{test.svg}}`

- Egy fájl optimalizálása és az eredmény mentése egy másik fájlba:

`svgo {{test.svg}} -o {{test.min.svg}}`

- Egy könyvtárban lévő összes SVG-fájl optimalizálása (felülírja az eredeti fájlokat):

`svgo -f {{path/to/directory/with/svg/files}}`

- Egy könyvtáron belüli összes SVG-fájl optimalizálása és az eredményül kapott fájlok mentése egy másik könyvtárba:

`svgo -f {{path/to/input/directory}} -o {{path/to/output/directory}}`

- Egy másik parancsból átadott SVG-tartalom optimalizálása és az eredmény mentése egy fájlba:

`{{cat test.svg}} | svgo -i - -o {{test.min.svg}}`

- Egy fájl optimalizálása és az eredmény kinyomtatása:

`svgo {{test.svg}} -o -`

- Elérhető bővítmények megjelenítése:

`svgo --show-plugins`
