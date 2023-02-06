# sqsc

> Parancssori AWS Simple Queue Service kliens. További információ: <https://github.com/yongfei25/sqsc>.

- Listázza az összes várólistát:

`sqsc lq {{queue_prefix}}`

- Egy várólistában lévő összes üzenet listázása:

`sqsc ls {{queue_name}}`

- Az összes üzenet másolása az egyik várólistából egy másikba:

`sqsc cp {{source_queue}} {{destination_queue}}`

- Az összes üzenet áthelyezése az egyik várólistából a másikba:

`sqsc mv {{source_queue}} {{destination_queue}}`

- Egy várólista leírása:

`sqsc describe {{queue_name}}`

- SQL-szintaxis segítségével lekérdezni egy várólistát:

`sqsc query "SELECT body FROM {{queue_name}} WHERE body LIKE '%user%'"`

- A várólistából az összes üzenetet a jelenlegi munkakönyvtárban lévő helyi SQLite adatbázisba húzza:

`sqsc pull {{queue_name}}`
