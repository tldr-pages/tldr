# doctl տվյալների բազաների կրկնօրինակ

> Կառավարեք տվյալների բազայի կլաստերի հետ կապված միայն կարդալու կրկնօրինակները:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/databases/replica/>:.

- Գործարկեք `doctl databases replica` հրամանը մուտքի նշանով.:

`doctl {{[d|databases]}} {{[r|replica]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Ստացեք տեղեկատվություն միայն կարդալու տվյալների բազայի կրկնօրինակի մասին.:

`doctl {{[d|databases]}} {{[r|replica]}} {{[g|get]}} {{database_id}} {{replica_name}}`

- Առբերեք միայն կարդալու տվյալների բազայի կրկնօրինակների ցանկը.:

`doctl {{[d|databases]}} {{[r|replica]}} {{[ls|list]}} {{database_id}}`

- Ստեղծեք տվյալների բազայի միայն կարդալու կրկնօրինակ.:

`doctl {{[d|databases]}} {{[r|replica]}} {{[c|create]}} {{database_id}} {{replica_name}}`

- Ջնջել տվյալների բազայի միայն կարդալու կրկնօրինակը.:

`doctl {{[d|databases]}} {{[r|replica]}} {{[rm|delete]}} {{database_id}} {{replica_name}}`
