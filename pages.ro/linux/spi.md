# spi

> Un manager de pachete meta care se ocupă atât de pachete, cât și de slackbuilds.
> Mai multe informaţii: <https://github.com/gapan/spi>

- Actualizați lista de pachete disponibile și slackbuilds:

`spi --update`

- Instalați un pachet sau slackbuild:

`spi --install {{package/slackbuild_name}}`

- Upgrade toate pachetele instalate la cele mai recente versiuni disponibile:

`spi --upgrade`

- Localizați pachetele sau slackbuild-urile de interes după numele sau descrierea pachetului:

`spi {{search_terms}}`

- Afișează informații despre un pachet sau slackbuild:

`spi --show {{package/slackbuild_name}}`

- Purge pachetul local și cache-uri slackbuild:

`spi --clean`
