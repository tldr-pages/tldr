# redis-cli

> Deschide o conexiune la un server Redis.
> Mai multe informaţii: <https://redis.io/topics/rediscli>

- Conectați-vă la serverul local:

`redis-cli`

- Conectați-vă la un server la distanță pe portul implicit (6379):

`redis-cli -h {{host}}`

- Conectați-vă la un server de la distanță specificând un număr de port:

`redis-cli -h {{host}} -p {{port}}`

- Conectarea la un server de la distanță specificând un URI:

`redis-cli -u {{uri}}`

- Specificați o parolă:

`redis-cli -a {{password}}`

- Execută comanda Redis:

`redis-cli {{redis_command}}`

- Conectați-vă la clusterul local:

`redis-cli -c`
