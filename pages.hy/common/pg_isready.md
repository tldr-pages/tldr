# pg_պատրաստ է

> Ստուգեք PostgreSQL սերվերի միացման կարգավիճակը:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pg-isready.html>:.

- Ստուգեք կապը.:

`pg_isready`

- Ստուգեք կապը կոնկրետ հոսթի անվան և նավահանգստի հետ.:

`pg_isready {{[-h|--host]}} {{hostname}} {{[-p|--port]}} {{port}}`

- Ստուգեք կապը՝ ցուցադրելով հաղորդագրություն միայն այն դեպքում, երբ կապը ձախողվի.:

`pg_isready {{[-q|--quiet]}}`
