# consul-kv

> Distributed key-value store with health checking and service discovery.
> More information: <https://learn.hashicorp.com/consul/getting-started/kv>.

- Read a value from the key-value store:

`consul kv get {{key}}`

- Store a new key-value pair:

`consul kv put {{key}} {{value}}`

- Delete a key-value pair:

`consul kv delete {{key}}`
