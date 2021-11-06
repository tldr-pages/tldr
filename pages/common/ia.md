# ia

> Command-line tool to interact with `archive.org`.
> More information: <https://archive.org/services/docs/api/internetarchive/cli.html>.

- Configure `ia` with API keys (some functions won't work without this step):

`ia configure`

- Upload one or more item to `archive.org`:

`ia upload {{identifier_value}} {{path/to/file}} --metadata="{{mediatype_value}}" --metadata="{{metadata_value}}"`

- Download one or more items from `archive.org`:

`ia download {{item_value}}`

- Delete item(s) from archive.org:

`ia delete {{identifier_value}} {{file_value}}`

- Search on archive.org, returning results as JSON:

`ia search 'subject:{{subject_value}} collection:{{collection_value}}`
