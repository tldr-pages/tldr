# magento

> Un CLI pentru gestionarea cadrului PHP Magento.
> Mai multe informaţii: <https://magento.com>

- Activați unul sau mai multe module separate de spațiu:

`magento module:enable {{module(s)}}`

- Dezactivați unul sau mai multe module separate de spațiu:

`magento module:disable {{module(s)}}`

- Actualizarea bazei de date după activarea modulelor:

`magento setup:upgrade`

- Actualizați configurația injecției de cod și dependență:

`magento setup:di:compile`

- Implementarea activelor statice:

`magento setup:static-content:deploy`

- Activează modul de întreținere:

`magento maintenance:enable`

- Dezactivați modul de întreținere:

`magento maintenance:disable`

- Listează toate comenzile disponibile:

`magento list`
