# pg_restore

> Վերականգնել PostgreSQL տվյալների բազան pg_dump-ի կողմից ստեղծված արխիվային ֆայլից:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgrestore.html>:.

- Վերականգնել արխիվը գոյություն ունեցող տվյալների բազայում.:

`pg_restore {{[-d|--dbname]}} {{db_name}} {{archive_file.dump}}`

- Նույնը, ինչ վերևում, հարմարեցրեք օգտվողի անունը.:

`pg_restore {{[-U|--username]}} {{username}} {{[-d|--dbname]}} {{db_name}} {{archive_file.dump}}`

- Նույնը, ինչ վերևում, հարմարեցրեք հոսթն ու նավահանգիստը.:

`pg_restore {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-d|--dbname]}} {{db_name}} {{archive_file.dump}}`

- Թվարկեք արխիվում ներառված տվյալների բազայի օբյեկտները.:

`pg_restore {{[-l|--list]}} {{archive_file.dump}}`

- Մաքրել տվյալների բազայի օբյեկտները նախքան դրանք ստեղծելը.:

`pg_restore {{[-c|--clean]}} {{[-d|--dbname]}} {{db_name}} {{archive_file.dump}}`

- Վերականգնումը կատարելու համար օգտագործեք բազմաթիվ աշխատանքներ.:

`pg_restore {{[-j|--jobs]}} {{2}} {{[-d|--dbname]}} {{db_name}} {{archive_file.dump}}`
