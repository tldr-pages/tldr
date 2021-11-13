# ia

> Command-line tool to interact with `archive.org`.
> More information: <https://archive.org/services/docs/api/internetarchive/cli.html>.

- Configure `ia` with API keys (some functions won't work without this step):

`ia configure`

- Upload one or more items to `archive.org`:

`ia upload {{identifier}} {{path/to/file}} --metadata="{{mediatype:data}}" --metadata="{{title:example}}"`

- Download one or more items from `archive.org`:

`ia download {{item}}`

- Delete one or more items from `archive.org`:

`ia delete {{identifier}} {{file}}`

- Search on `archive.org`, returning results as JSON:

`ia search '{{subject:"subject" collection:collection}}'`
