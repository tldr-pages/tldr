# mongoexport

> Produceți exporturi de date stocate într-o instanță MongoDB formatat ca JSON sau CSV.
> Mai multe informaţii: <https://docs.mongodb.com/database-tools/mongoexport/>

- Exportați o colecție în stdout, formatat ca JSON:

`mongoexport --uri={{connection_string}} --collection={{collection_name}}`

- Exportați documentele din colecția specificată care se potrivesc unei interogări într-un fișier JSON:

`mongoexport --db={{database_name}} --collection={{collection_name}} --query="{{query_object}}" --out={{path/to/file.json}}`

- Exportați documente ca matrice JSON în loc de un obiect pe linie:

`mongoexport --collection={{collection_name}} --jsonArray`

- Exportați documente într-un fișier CSV:

`mongoexport --collection={{collection_name}} --type={{csv}} --fields="{{field1,field2,...}}" --out={{path/to/file.csv}}`

- Exportați documente care se potrivesc cu interogarea din fișierul specificat într-un fișier CSV, omitând lista numelor de câmpuri de pe prima linie:

`mongoexport --collection={{collection_name}} --type={{csv}} --fields="{{field1,field2,...}}" --queryFile={{path/to/file}} --noHeaderLine --out={{path/to/file.csv}}`

- Exportați documente în stdout, formatate ca JSON lizibil de om:

`mongoexport --uri={{mongodb_uri}} --collection={{collection_name}} --pretty`

- Ajutor pentru afișare:

`mongoexport --help`
