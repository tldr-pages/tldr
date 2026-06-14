# mongorestore

> Կոմունալ հավաքածու կամ տվյալների բազա երկուական աղբավայրից MongoDB օրինակ ներմուծելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.mongodb.com/docs/database-tools/mongorestore/>:.

- Ներմուծեք BSON տվյալների աղբավայրը գրացուցակից MongoDB տվյալների բազա.:

`mongorestore --db {{database_name}} {{path/to/directory}}`

- Ներմուծեք BSON տվյալների աղբավայրը գրացուցակից տվյալ տվյալների բազա MongoDB սերվերի հոսթում, որն աշխատում է տվյալ նավահանգստում, օգտատիրոջ իսկորոշմամբ (օգտատիրոջը կառաջարկվի գաղտնաբառ):

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/directory}} --password`

- Ներմուծեք հավաքածու BSON ֆայլից MongoDB տվյալների բազա.:

`mongorestore --db {{database_name}} {{path/to/file}}`

- Ներմուծեք հավաքածու BSON ֆայլից տվյալ տվյալների բազա MongoDB սերվերի հոսթում, որն աշխատում է տվյալ նավահանգստում, օգտատիրոջ իսկորոշմամբ (օգտատիրոջը կառաջարկվի գաղտնաբառ):

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/file}} --password`
