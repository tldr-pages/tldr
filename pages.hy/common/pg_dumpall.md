# pg_dumpal

> Քաղեք PostgreSQL տվյալների բազայի կլաստերը սցենարի ֆայլի կամ արխիվային այլ ֆայլի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pg-dumpall.html>:.

- Թափել բոլոր տվյալների բազաները.:

`pg_dumpall > {{path/to/file.sql}}`

- Թափել բոլոր տվյալների բազաները՝ օգտագործելով հատուկ օգտանուն.:

`pg_dumpall {{[-U|--username]}} {{username}} > {{path/to/file.sql}}`

- Նույնը, ինչ վերևում, հարմարեցրեք հոսթն ու նավահանգիստը.:

`pg_dumpall {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} > {{output_file.sql}}`

- Թափել միայն տվյալների բազայի տվյալները SQL-script ֆայլի մեջ.:

`pg_dumpall {{[-a|--data-only]}} > {{path/to/file.sql}}`

- Թափել միայն սխեման (տվյալների սահմանումները) SQL-script ֆայլի մեջ.:

`pg_dumpall {{[-s|--schema-only]}} > {{output_file.sql}}`
