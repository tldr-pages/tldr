# redis-cli

> Kapcsolatot nyit egy Redis-kiszolgálóhoz. További információ: <https://redis.io/topics/rediscli>.

- Csatlakozás a helyi kiszolgálóhoz:

`redis-cli`

- Csatlakozás egy távoli kiszolgálóhoz az alapértelmezett porton (6379):

`redis-cli -h {{host}}`

- Csatlakozás egy távoli kiszolgálóhoz egy portszám megadásával:

`redis-cli -h {{host}} -p {{port}}`

- Csatlakozás egy URI-t megadó távoli kiszolgálóhoz:

`redis-cli -u {{uri}}`

- Jelszó megadása:

`redis-cli -a {{password}}`

- Redis parancs végrehajtása:

`redis-cli {{redis_command}}`

- Csatlakozás a helyi fürthöz:

`redis-cli -c`
