# redis-server

> Tartós kulcs-érték adatbázis. További információ: <https://redis.io>.

- Indítsa el a Redis szervert az alapértelmezett porton (6379), és írja a naplókat a `stdout` címre:

`redis-server`

- Indítsa el a Redis kiszolgálót az alapértelmezett porton, háttérfolyamatként:

`redis-server --daemonize yes`

- Indítsa el a Redis kiszolgálót a megadott portot használva háttérfolyamatként:

`redis-server --port {{port}} --daemonize yes`

- A Redis kiszolgáló indítása egyéni konfigurációs fájl segítségével:

`redis-server {{path/to/redis.conf}}`

- Redis kiszolgáló indítása bő naplózással:

`redis-server --loglevel {{warning|notice|verbose|debug}}`
