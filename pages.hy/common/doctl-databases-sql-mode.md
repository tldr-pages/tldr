# doctl տվյալների բազաներ sql-mode

> Դիտեք և կազմաձևեք MySQL տվյալների բազայի կլաստերի գլոբալ SQL ռեժիմները:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/databases/sql-mode/>:.

- Գործարկեք `doctl databases sql-mode` հրամանը մուտքի նշանով.:

`doctl {{[d|databases]}} {{[sm|sql-mode]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Ստացեք MySQL տվյալների բազայի կլաստերի SQL ռեժիմները.:

`doctl {{[d|databases]}} {{[sm|sql-mode]}} {{[g|get]}} {{database_id}}`

- Վերագրեք MySQL տվյալների բազայի կլաստերի SQL ռեժիմները նշված ռեժիմներին.:

`doctl {{[d|databases]}} {{[sm|sql-mode]}} {{[s|set]}} {{database_id}} {{sql_mode_1 sql_mode_2 ...}}`
