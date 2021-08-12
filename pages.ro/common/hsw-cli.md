# hsw-cli

> Instrumentul REST de linie de comandă pentru portofelul strângere de mână.
> Mai multe informaţii: <https://npmjs.com/package/hs-client>

- Deblocați portofelul curent (timeout în secunde):

`hsw-cli unlock {{passphrase}} {{timeout}}`

- Blocați portofelul curent:

`hsw-cli lock`

- Vezi detaliile portofelului curent:

`hsw-cli get`

- Vizualizaţi soldul portofelului curent:

`hsw-cli balance`

- Vizualizați istoricul tranzacțiilor portofelului curent:

`hsw-cli history`

- Trimiteți o tranzacție cu suma specificată a monedei la o adresă:

`hsw-cli send {{address}} {{1.05}}`

- Vizualizați tranzacțiile în așteptare ale portofelului curent:

`hsw-cli pending`

- Vezi detalii despre o tranzacție:

`hsw-cli tx {{transaction_hash}}`
