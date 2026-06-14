# mysqlsh

> Ընդլայնված հաճախորդ MySQL-ի համար, որն աջակցում է SQL-ին, JavaScript-ին և Python-ին:.
> Այն առաջարկում է InnoDB կլաստերների և փաստաթղթերի խանութների հավաքածուների կառավարման գործառույթներ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/mysqlsh>:.

- Սկսեք MySQL Shell-ը ինտերակտիվ ռեժիմով.:

`mysqlsh`

- Միացեք MySQL սերվերին.:

`mysqlsh --user {{username}} --host {{hostname}} --port {{port}}`

- Կատարեք SQL հայտարարություն սերվերի վրա և դուրս եկեք.:

`mysqlsh --user {{username}} --execute '{{sql_statement}}'`

- Սկսեք MySQL Shell-ը JavaScript ռեժիմով.:

`mysqlsh --js`

- Սկսեք MySQL Shell-ը Python ռեժիմում.:

`mysqlsh --py`

- Ներմուծեք JSON փաստաթղթերը MySQL հավաքածու.:

`mysqlsh --import {{path/to/file.json}} --schema {{schema_name}} --collection {{collection_name}}`

- Միացնել բառախաղ ելքը.:

`mysqlsh --verbose`
