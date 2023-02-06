# genid

> Azonosítók, például hópelyhek, UUID-k és egy új GAID generálása. További információ: <https://github.com/bleonard252/genid>.

- UUIDv4 generálása:

`genid uuid`

- UUIDv5 generálása egy névtér UUID és egy adott név felhasználásával:

`genid uuidv5 {{{ce598faa-8dd0-49ee-8525-9e24fff71dca}}} {{name}}`

- Discord hópehely generálása, hátul lévő újsor nélkül (hasznos a shell szkriptekben):

`genid --script snowflake`

- Generikus névtelen azonosító generálása egy konkrét "valódi azonosítóval":

`genid gaid {{real_id}}`

- Snowflake generálása egy adott dátumra beállított epochával:

`genid snowflake --epoch={{unix_epoch_time}}`
