# pg_basebackup

> Վերցրեք գործարկվող PostgreSQL կլաստերի հիմնական կրկնօրինակը:.
> Օգտագործվում է լրիվ կամ աստիճանաբար կրկնօրինակումների, ժամանակի ընթացքում վերականգնման կամ կրկնօրինակման սպասման ռեժիմների ստեղծման համար:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgbasebackup.html>:.

- Վերցրեք բազային կրկնօրինակում հեռավոր PostgreSQL սերվերից.:

`pg_basebackup {{[-h|--host]}} {{host}} {{[-D|--pgdata]}} {{path/to/backup_dir}}`

- Վերցրեք կրկնօրինակում` ցույց տրված առաջընթացով.:

`pg_basebackup {{[-h|--host]}} {{host}} {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-P|--progress]}}`

- Ստեղծեք սեղմված կրկնօրինակ (`gzip`) tar ձևաչափով.:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-F|--format]}} {{[t|tar]}} {{[-z|--gzip]}}`

- Ստեղծեք լրացուցիչ կրկնօրինակում, օգտագործելով նախորդ մանիֆեստի ֆայլը.:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-i|--incremental]}} {{path/to/old_manifest}}`

- Գրեք վերականգնման կոնֆիգուրացիա՝ սպասման ռեժիմը կարգավորելու համար.:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-R|--write-recovery-conf]}}`

- Տեղափոխեք սեղանի տարածքը կրկնօրինակման ժամանակ.:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-T|--tablespace-mapping]}} {{path/to/old_tablespace}}={{path/to/new_tablespace}}`

- Սահմանափակեք փոխանցման արագությունը՝ սերվերի բեռը նվազեցնելու համար.:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-r|--max-rate]}} {{100M}}`

- Հոսեք WAL տեղեկամատյանները պահուստավորումը վերցնելիս.:

`pg_basebackup {{[-D|--pgdata]}} {{path/to/backup_dir}} {{[-X|--wal-method]}} stream`
