# ia

> Command-line tool to interact with archive.org.
> More information: <https://archive.org/services/docs/api/internetarchive/cli.html>.

- Configure ia to get your API keys; certain functions won't work without this step:

`ia configure`

- Upload item(s) to archive.org:

`ia upload {{identifier_value}} {{file_name}} --metadata="{{mediatype_value}}" --metadata="{{metadata_value}}"`

- Download item(s) from archive.org:

`ia download {{item_value}}`

- Delete item(s) from archive.org:

`ia delete {{identifier_value}} {{file_value}}`

- Search on archive.org; results are retrieved in JSON format:

`ia search 'subject:{{subject_value}} collection:{{collection_value}}`
