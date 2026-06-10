# pg_verifybackup

> Ստուգեք PostgreSQL կլաստերի բազային կրկնօրինակի ամբողջականությունը:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgverifybackup.html>:.

- Ստուգեք հատուկ գրացուցակում պահված կրկնօրինակը.:

`pg_verifybackup {{path/to/backup}}`

- Ստուգեք կրկնօրինակը, որը ցույց է տալիս առաջընթացի մասին տեղեկությունները.:

`pg_verifybackup {{[-P|--progress]}} {{path/to/backup}}`

- Ստուգեք կրկնօրինակը և անմիջապես դուրս եկեք առաջին սխալի դեպքում.:

`pg_verifybackup {{[-e|--exit-on-error]}} {{path/to/backup}}`

- Ստուգեք կրկնօրինակը, որը անտեսում է որոշակի ֆայլեր կամ գրացուցակներ.:

`pg_verifybackup {{[-i|--ignore]}} {{path/to/file_or_directory}} {{path/to/backup}}`

- Ստուգեք կրկնօրինակը մանիֆեստի ֆայլով այլ վայրում.:

`pg_verifybackup {{[-m|--manifest-path]}} {{path/to/backup_manifest}} {{path/to/backup}}`

- Ցուցադրել օգնությունը.:

`pg_verifybackup {{[-?|--help]}}`
