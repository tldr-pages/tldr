# cryptsetup

> Gestisce volumi crittografati `dm-crypt` e LUKS (Linux Unified Key Setup).
> Alcuni sottocomandi come `luksFormat` hanno la propria documentazione d'uso.
> Maggiori informazioni: <https://manned.org/cryptsetup>.

- Inizializza un volume LUKS con una passphrase (sovrascrive tutti i dati sulla partizione):

`cryptsetup luksFormat {{/dev/sdXY}}`

- Apre un volume LUKS e crea un mapping decrittografato su `/dev/mapper/mapping_name`:

`cryptsetup open {{/dev/sdXY}} {{mapping_name}}`

- Mostra informazioni su un mapping:

`cryptsetup status {{mapping_name}}`

- Rimuove un mapping esistente:

`cryptsetup close {{mapping_name}}`

- Cambia la passphrase di un volume LUKS:

`cryptsetup luksChangeKey {{/dev/sdXY}}`

- Mostra le informazioni dell'intestazione LUKS e i metadati degli slot di chiave di un dispositivo crittografato:

`cryptsetup luksDump {{/dev/sdXY}}`
