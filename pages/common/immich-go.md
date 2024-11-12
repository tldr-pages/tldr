# immich-go

> Immich-Go is an open-source tool designed to streamline uploading large photo collections to your self-hosted Immich server.
> See also: `immich-cli`.
> More information: <https://github.com/simulot/immich-go>.

- Upload a Google Photos takeout file to Immich server:

`immich-go -server={{server_url}} -key={{server_key}} upload {{path/to/takeout_file.zip}}`

- Import photos captured on June 2019, while auto-generating albums:

`immich-go -server={{server_url}} -key={{server_key}} upload -create-albums -google-photos -date={{2019-06}} {{path/to/takeout_file.zip}}`

- Upload a takeout file using server and key from a config file:

`immich-go -use-configuration={{~/.immich-go/immich-go.json}} upload {{path/to/takeout_file.zip}}`

- Examine Immich server content, remove less quality images, and preserve albums:

`immich-go -server={{server_url}} -key={{server_key}} duplicate -yes`

- Delete all albums created with the pattern "YYYY-MM-DD":

`immich-go -server={{server_url}} -key={{server_key}} tool album delete {{\d{4}-\d{2}-\d{2}}}`
