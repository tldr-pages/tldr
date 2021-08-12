# consul-kv

> Magazin de chei-valoare distribuită cu verificarea stării de sănătate și descoperirea serviciilor.
> Mai multe informaţii: <https://learn.hashicorp.com/consul/getting-started/kv>

- Citiți o valoare din magazinul cheie-valoare:

`consul kv get {{key}}`

- Stocați o nouă pereche cheie-valoare:

`consul kv put {{key}} {{value}}`

- Ștergeți o pereche cheie-valoare:

`consul kv delete {{key}}`
