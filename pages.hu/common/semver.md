# semver

> Szemantikus verziójú karakterlánc-elemző. További információ: <https://github.com/npm/node-semver>.

- Ellenőrzi, hogy egy verziósztring megfelel-e a szemantikus verzióformátumnak (üres sztringet ír ki, ha nem felel meg):

`semver {{1.2}}`

- Egy verziósztringet konvertál a szemantikus verziókezelési formátumba:

`semver --coerce {{1.2}}`

- Annak vizsgálata, hogy a `1.2.3` megfelel-e a `^1.0` tartománynak (üres karakterláncot ír ki, ha nem felel meg):

`semver {{1.2.3}} --range "{{^1.0}}"`

- Tesztelés több tartományban:

`semver {{1.2.3}} --range {{">=1.0"}} {{"<2.0"}}`

- Több verziósztring tesztelése, és csak az egyezőket adja vissza:

`semver {{1.2.3}} {{2.0.0}} --range "{{^1.0}}"`
