# doctl տվյալների բազաներ

> Կառավարեք ձեր MySQL, Redis, PostgreSQL և MongoDB տվյալների բազայի ծառայությունները:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/databases/>:.

- Գործարկեք `doctl databases` հրամանը մուտքի նշանով.:

`doctl {{[d|databases]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Ստացեք մանրամասներ տվյալների բազայի կլաստերի համար.:

`doctl {{[d|databases]}} {{[g|get]}}`

- Թվարկեք ձեր տվյալների բազայի կլաստերները.:

`doctl {{[d|databases]}} {{[ls|list]}}`

- Ստեղծեք տվյալների բազայի կլաստեր.:

`doctl {{[d|databases]}} {{[c|create]}} {{database_name}}`

- Ջնջել կլաստերը.:

`doctl {{[d|databases]}} {{[rm|delete]}} {{database_id}}`
