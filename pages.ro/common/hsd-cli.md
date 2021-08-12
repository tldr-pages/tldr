# hsd-cli

> Instrumentul REST pentru linia de comandă pentru blockchain Handshake.
> Mai multe informaţii: <https://handshake.org>

- Recuperați informații despre serverul curent:

`hsd-cli info`

- Difuzarea unei tranzacții locale:

`hsd-cli broadcast {{transaction_hex}}`

- Recuperarea unui instantaneu mempool:

`hsd-cli mempool`

- Vizualizați o tranzacție după adresă sau hash:

`hsd-cli tx {{address_or_hash}}`

- Vezi o monedă după indexul sau adresa hash:

`hsd-cli coin {{hash_index_or_address}}`

- Vizualizaţi un bloc de înălţime sau hash:

`hsd-cli block {{height_or_hash}}`

- Resetați lanțul la blocul specificat:

`hsd-cli reset {{height_or_hash}}`

- Execută o comandă RPC:

`hsd-cli rpc {{command}} {{args}}`
