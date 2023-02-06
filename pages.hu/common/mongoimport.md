# mongoimport

> Tartalom importálása JSON, CSV vagy TSV fájlból egy MongoDB adatbázisba. További információ: <https://docs.mongodb.com/database-tools/mongoimport/>.

- JSON fájl importálása egy adott gyűjteménybe:

`mongoimport --file={{path/to/file.json}} --uri={{mongodb_uri}} --collection={{collection_name}}`

- Importál egy CSV-fájlt, a mezőnevek meghatározásához a fájl első sorát használja:

`mongoimport --type={{csv}} --file={{path/to/file.csv}} --db={{database_name}} --collection={{collection_name}}`

- JSON tömb importálása, minden egyes elemet külön dokumentumként használva:

`mongoimport --jsonArray --file={{path/to/file.json}}`

- JSON-fájl importálása egy adott mód és egy lekérdezés segítségével a meglévő dokumentumokkal való egyezéshez:

`mongoimport --file={{path/to/file.json}} --mode={{delete|merge|upsert}} --upsertFields="{{field1,field2,...}}"`

- CSV-fájl importálása, a mezőnevek beolvasása egy külön CSV-fájlból és az üres értékekkel rendelkező mezők figyelmen kívül hagyása:

`mongoimport --type={{csv}} --file={{path/to/file.csv}} --fieldFile={{path/to/field_file.csv}} --ignoreBlanks`

- Súgó megjelenítése:

`mongoimport --help`
