# consul-kv

> Elosztott kulcsérték-tároló állapotellenőrzéssel és szolgáltatáskereséssel. További információ: <https://learn.hashicorp.com/consul/getting-started/kv>.

- Érték beolvasása a kulcs-értéktárolóból:

`consul kv get {{key}}`

- Új kulcs-érték pár tárolása:

`consul kv put {{key}} {{value}}`

- Kulcs-érték pár törlése:

`consul kv delete {{key}}`
