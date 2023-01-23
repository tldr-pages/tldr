# mongod

> A MongoDB adatbázis-kiszolgáló. További információ: <https://docs.mongodb.com/manual/reference/program/mongod>.

- Konfigurációs fájl megadása:

`mongod --config {{path/to/file}}`

- Adja meg a portot, amelyen hallgatni kell:

`mongod --port {{port}}`

- Adja meg az adatbázis profilozási szintjét. A 0 kikapcsolt, az 1 csak lassú műveletek, a 2 minden:

`mongod --profile {{0|1|2}}`
