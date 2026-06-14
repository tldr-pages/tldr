# hsd-cli

> REST գործիքը Handshake blockchain-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://handshake.org/>:.

- Ստացեք տեղեկատվություն ընթացիկ սերվերի մասին.:

`hsd-cli info`

- Հեռարձակել տեղական գործարք.:

`hsd-cli broadcast {{transaction_hex}}`

- Առբերեք mempool snapshot:

`hsd-cli mempool`

- Դիտեք գործարքը հասցեով կամ հեշով.:

`hsd-cli tx {{address_or_hash}}`

- Դիտեք մետաղադրամն իր հեշ ինդեքսով կամ հասցեով.:

`hsd-cli coin {{hash_index_or_address}}`

- Դիտեք բլոկը ըստ բարձրության կամ հեշի.:

`hsd-cli block {{height_or_hash}}`

- Վերականգնել շղթան նշված բլոկին.:

`hsd-cli reset {{height_or_hash}}`

- Կատարեք RPC հրաման.:

`hsd-cli rpc {{command}} {{args}}`
