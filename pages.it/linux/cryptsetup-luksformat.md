# cryptsetup luksFormat

> Inizializza una partizione LUKS e lo slot di chiave iniziale (0) con una passphrase o un keyfile.
> Nota: Questa operazione sovrascrive tutti i dati sulla partizione.
> Maggiori informazioni: <https://manned.org/cryptsetup-luksFormat>.

- Inizializza un volume LUKS con una passphrase:

`cryptsetup luksFormat {{/dev/sdXY}}`

- Inizializza un volume LUKS con un keyfile:

`cryptsetup luksFormat {{/dev/sdXY}} {{path/to/keyfile}}`

- Inizializza un volume LUKS con una passphrase e imposta la sua etichetta:

`cryptsetup luksFormat --label {{label}} {{/dev/sdXY}}`
