# mongoimport

> Imports content from a JSON, CSV, or TSV file into a MongoDB.
> More information: <https://docs.mongodb.com/database-tools/mongoimport/>.

- Import a JSON file into a specific collection:

`mongoimport --file={{path/to/file}} --uri={{mongodb_uri}} --collection={{collection_name}}`

- Import a CSV file using the first line as the field list into the localhost instance:

`mongoimport --type={{csv}} --file{{path/to/file}} --db={{database_name}} --collection={{collection_name}}`

- Import a JSON array using each element as a MongoDB document:

`mongoimport --jsonArray --file={{path/to/file}}`

- Import a JSON file using a specific mode and a query to match already existing documents:

`mongoimport --file={{path/to/file}} --mode={{delete|merge|upsert}} --upsertFields="{{field1,field2,...}}"`

- Import a CSV using a file with field names for the columns and ignoring fields with empty values:

`mongoimport  --type={{csv}} --file={{path/to/file} --fieldFile={{path/to/field_file}} --ignoreBlanks`
