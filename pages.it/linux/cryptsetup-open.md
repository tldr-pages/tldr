# cryptsetup open

> Crea un mapping decrittografato di un volume crittografato.
> Nota: Con TRIM abilitato, si può verificare una minima perdita di dati sotto forma di informazioni sui blocchi liberati, forse sufficienti per determinare il filesystem in uso.
> Tuttavia, è consigliabile abilitarlo comunque, perché i dati al suo interno sono ancora al sicuro e gli SSD senza TRIM si usurano più velocemente.
> Maggiori informazioni: <https://manned.org/cryptsetup-open>.

- Apre un volume LUKS e crea un mapping decrittografato su `/dev/mapper/mapping_name`:

`cryptsetup open {{/dev/sdXY}} {{nome_mapping}}`

- Utilizza un keyfile invece di una passphrase:

`cryptsetup open {{[-k|--key-file]}} {{path/to/file}} {{/dev/sdXY}} {{nome_mapping}}`

- Permette l'uso di TRIM sul dispositivo:

`cryptsetup open --allow-discards {{/dev/sdXY}} {{nome_mapping}}`

- Scrive l'opzione `--allow-discards` nell'intestazione LUKS (l'opzione verrà quindi sempre utilizzata quando si apre il dispositivo):

`cryptsetup open --allow-discards --persistent {{/dev/sdXY}} {{nome_mapping}}`

- Apre un volume LUKS e rende il mapping decrittografato di sola lettura:

`cryptsetup open {{[-r|--readonly]}} {{/dev/sdXY}} {{nome_mapping}}`
