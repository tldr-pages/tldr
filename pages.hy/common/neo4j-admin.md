# neo4j-admin

> Կառավարեք և կառավարեք Neo4j DBMS (Տվյալների բազայի կառավարման համակարգ):.
> Տես նաև՝ `cypher-shell`, `mysqld`:.
> Լրացուցիչ տեղեկություններ. <https://neo4j.com/docs/operations-manual/current/neo4j-admin-neo4j-cli/>:.

- Սկսեք DBMS-ը.:

`neo4j-admin server start`

- Դադարեցրեք DBMS-ը.:

`neo4j-admin server stop`

- Սահմանեք կանխադրված `neo4j` օգտվողի սկզբնական գաղտնաբառը (DBMS-ի առաջին մեկնարկի նախապայման).:

`neo4j-admin dbms set-initial-password {{database_name}}`

- Ստեղծեք օֆլայն տվյալների բազայի արխիվ (աղբավայր) `database_name.dump` անունով ֆայլում՝:

`neo4j-admin database dump --to-path={{path/to/directory}} {{database_name}}`

- Բեռնել տվյալների բազան `database_name.dump` անունով արխիվից:

`neo4j-admin database load --from-path={{path/to/directory}} {{database_name}} --overwrite-destination=true`

- Բեռնել տվյալների բազա նշված արխիվային ֆայլից `stdin` միջոցով:

`neo4j-admin < {{path/to/file.dump}} database load --from-stdin {{database_name}} --overwrite-destination=true`

- Ցուցադրել օգնությունը.:

`neo4j-admin --help`
