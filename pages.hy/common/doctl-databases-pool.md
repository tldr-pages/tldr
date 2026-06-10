# doctl տվյալների բազաների լողավազան

> Կառավարեք կապի լողավազանները ձեր տվյալների բազայի կլաստերի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/databases/pool/>:.

- Գործարկեք `doctl databases pool` հրամանը մուտքի նշանով.:

`doctl {{[d|databases]}} {{[p|pool]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Ստացեք տեղեկատվություն տվյալների բազայի միացման լողավազանի մասին.:

`doctl {{[d|databases]}} {{[p|pool]}} {{[g|get]}} {{database_id}} {{pool_name}}`

- Ցուցակեք կապի լողավազանները տվյալների բազայի կլաստերի համար.:

`doctl {{[d|databases]}} {{[p|pool]}} {{[ls|list]}} {{database_id}}`

- Ստեղծեք կապի լողավազան տվյալների բազայի համար.:

`doctl {{[d|databases]}} {{[p|pool]}} {{[c|create]}} {{database_id}} {{pool_name}} --db {{new_pool_name}} --size {{pool_size}}`

- Ջնջել տվյալների բազայի միացման լողավազանը.:

`doctl {{[d|databases]}} {{[p|pool]}} {{[rm|delete]}} {{database_id}} {{pool_name}}`
