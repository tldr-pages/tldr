# texconfig

> Configure TeX Live or teTeX.
> Superseded in many cases by `tlmgr`.
> More information: <https://manned.org/texconfig>.

- Display the current TeX configuration:

`texconfig conf`

- Set the default paper size for supported programs:

`texconfig paper {{a4|letter|...}}`

- Set the default paper size for PDFTeX:

`texconfig pdftex paper {{a4|letter|...}}`

- Rebuild all TeX formats and font maps:

`texconfig init`

- Rebuild a specific format:

`texconfig init {{format}}`

- Refresh the TeX filename database:

`texconfig rehash`
