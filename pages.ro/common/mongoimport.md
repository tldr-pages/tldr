# mongoimport

> Importă conținut dintr-un fișier JSON, CSV sau TSV într-o bază de date MongoDB.
> Mai multe informaţii: <https://docs.mongodb.com/database-tools/mongoimport/>

- Importați un fișier JSON într-o anumită colecție:

`mongoimport --file={{path/to/file.json}} --uri={{mongodb_uri}} --collection={{collection_name}}`

- Importați un fișier CSV, utilizând prima linie a fișierului pentru a determina numele câmpurilor:

`mongoimport --type={{csv}} --file={{path/to/file.csv}} --db={{database_name}} --collection={{collection_name}}`

- Importați o matrice JSON, utilizând fiecare element ca document separat:

`mongoimport --jsonArray --file={{path/to/file.json}}`

- Importați un fișier JSON utilizând un anumit mod și o interogare pentru a se potrivi cu documentele existente:

`mongoimport --file={{path/to/file.json}} --mode={{delete|merge|upsert}} --upsertFields="{{field1,field2,...}}"`

- Importul unui fişier CSV, citirea numelor câmpurilor dintr-un fişier CSV separat şi ignorarea câmpurilor cu valori goale:

`mongoimport --type={{csv}} --file={{path/to/file.csv}} --fieldFile={{path/to/field_file.csv}} --ignoreBlanks`

- Ajutor pentru afișare:

`mongoimport --help`
