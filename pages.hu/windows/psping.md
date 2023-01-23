# psping

> Ping eszköz, amely TCP ping, késleltetés és sávszélesség mérést is tartalmaz. További információ: <https://learn.microsoft.com/sysinternals/downloads/psping>.

- Egy állomás pingelése ICMP használatával:

`psping {{hostname}}`

- Egy állomás pingelése egy TCP-porton keresztül:

`psping {{hostname}}:{{port}}`

- Adja meg a pingek számát és végezze el csendben:

`psping {{hostname}} -n {{pings}} -q`

- Pingelje a célpontot TCP-n keresztül 50-szer, és készítsen hisztogramot az eredményekről:

`psping {{hostname}}:{{port}} -q -n {{50}} -h`

- Használati információk megjelenítése:

`psping /?`
