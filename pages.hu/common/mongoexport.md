# mongoexport

> A MongoDB példányban tárolt adatok JSON vagy CSV formátumban történő exportálása. További információ: <https://docs.mongodb.com/database-tools/mongoexport/>.

- Gyűjtemény exportálása a `stdout` címre, JSON formátumban:

`mongoexport --uri={{connection_string}} --collection={{collection_name}}`

- A megadott gyűjteményben lévő, egy lekérdezésnek megfelelő dokumentumok exportálása egy JSON fájlba:

`mongoexport --db={{database_name}} --collection={{collection_name}} --query="{{query_object}}" --out={{path/to/file.json}}`

- A dokumentumok exportálása JSON tömbként, soronkénti egy objektum helyett:

`mongoexport --collection={{collection_name}} --jsonArray`

- Dokumentumok exportálása CSV fájlba:

`mongoexport --collection={{collection_name}} --type={{csv}} --fields="{{field1,field2,...}}" --out={{path/to/file.csv}}`

- A lekérdezésnek megfelelő dokumentumok exportálása a megadott fájlban egy CSV-fájlba, kihagyva a mezőnevek listáját az első sorban:

`mongoexport --collection={{collection_name}} --type={{csv}} --fields="{{field1,field2,...}}" --queryFile={{path/to/file}} --noHeaderLine --out={{path/to/file.csv}}`

- Dokumentumok exportálása a `stdout` címre, ember által olvasható JSON formátumban:

`mongoexport --uri={{mongodb_uri}} --collection={{collection_name}} --pretty`

- Súgó megjelenítése:

`mongoexport --help`
