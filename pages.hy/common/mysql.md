# mysql

> MySQL գործիքը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/mysql>:.

- Միացեք տվյալների շտեմարանին.:

`mysql {{database_name}}`

- Միացեք տվյալների շտեմարանին, օգտվողին կառաջարկվի գաղտնաբառ.:

`mysql {{[-u|--user]}} {{user}} {{[-p|--password]}} {{database_name}}`

- Միացեք տվյալների բազայի մեկ այլ հոսթի վրա.:

`mysql {{[-h|--host]}} {{database_host}} {{database_name}}`

- Միացեք տվյալների բազային Unix վարդակից.:

`mysql {{[-S|--socket]}} {{path/to/socket.sock}}`

- Կատարեք SQL հայտարարությունները սցենարի ֆայլում (խմբաքանակի ֆայլ).:

`mysql {{[-e|--execute]}} "source {{filename.sql}}" {{database_name}}`

- Վերականգնել տվյալների բազան `mysqldump`-ով ստեղծված կրկնօրինակից (օգտատիրոջը կպահանջվի գաղտնաբառ).:

`mysql < {{path/to/backup.sql}} {{[-u|--user]}} {{user}} {{[-p|--password]}} {{database_name}}`

- Վերականգնել բոլոր տվյալների բազաները կրկնօրինակից (օգտատիրոջը կառաջարկվի գաղտնաբառ).:

`mysql < {{path/to/backup.sql}} {{[-u|--user]}} {{user}} {{[-p|--password]}}`
