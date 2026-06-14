# pg_dump

> Քաղեք PostgreSQL տվյալների բազան սցենարի ֆայլի կամ արխիվային այլ ֆայլի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgdump.html>:.

- Թափել տվյալների բազան SQL-script ֆայլի մեջ.:

`pg_dump {{db_name}} > {{output_file.sql}}`

- Նույնը, ինչ վերևում, հարմարեցրեք օգտվողի անունը.:

`pg_dump {{[-U|--username]}} {{username}} {{db_name}} > {{output_file.sql}}`

- Նույնը, ինչ վերևում, հարմարեցրեք հոսթն ու նավահանգիստը.:

`pg_dump {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{db_name}} > {{output_file.sql}}`

- Տվյալների բազան լցրեք հատուկ ձևաչափով արխիվային ֆայլի մեջ.:

`pg_dump {{[-F|--format]}} {{[c|custom]}} {{db_name}} > {{output_file.dump}}`

- Թափել միայն տվյալների բազայի տվյալները SQL-script ֆայլի մեջ.:

`pg_dump {{[-a|--data-only]}} {{db_name}} > {{path/to/output_file.sql}}`

- Թափել միայն սխեման (տվյալների սահմանումները) SQL-script ֆայլի մեջ.:

`pg_dump {{[-s|--schema-only]}} {{db_name}} > {{path/to/output_file.sql}}`
