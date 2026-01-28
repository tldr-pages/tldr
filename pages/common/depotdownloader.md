# depotdownloader

> Content/depot downloader for Steam.
> More information: <https://github.com/SteamRE/DepotDownloader>.

- Download an app:

`depotdownloader -app {{108600}}`

- Download a specific depot into a custom output directory:

`depotdownloader -app {{108600}} -depot {{108603}} -dir {{path/to/directory}}`

- Download using a Steam account:

`depotdownloader -app {{108600}} -depot {{108603}} -username "{{gabecube}}"`

- Download a depot and remember the password for future downloads:

`depotdownloader -app {{108600}} -depot {{108603}} -username "{{gabecube}}" -remember-password`

- Download a specific depot manifest:

`depotdownloader -app {{346110}} -depot {{346111}} -manifest {{6154025194991279746}}`

- Download from a specific branch:

`depotdownloader -app {{108600}} -depot {{108603}} -branch "{{unstable}}"`

- Download only the internal manifest excluding content:

`depotdownloader -app {{108600}} -depot {{108603}} -manifest-only`

- Download workshop content using the pubfile/workshop id:

`depotdownloader -app {{108600}} -pubfile {{2503622437}}`
