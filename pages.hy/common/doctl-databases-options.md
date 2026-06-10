# doctl տվյալների բազաների ընտրանքներ

> Միացնել առկա ընտրանքների նավարկությունը տվյալների բազայի յուրաքանչյուր շարժիչի ներքո:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/databases/options/>:.

- Գործարկեք `doctl databases options` հրամանը մուտքի նշանով.:

`doctl {{[d|databases]}} {{[o|options]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Ստացեք տվյալների բազայի առկա շարժիչների ցանկը.:

`doctl {{[d|databases]}} {{[o|options]}} {{[eng|engines]}}`

- Վերցրեք տվյալների բազայի տվյալ շարժիչի համար հասանելի շրջանների ցանկը.:

`doctl {{[d|databases]}} {{[o|options]}} {{[r|regions]}} --engine {{pg|mysql|redis|mongodb}}`

- Վերցրեք տվյալների բազայի տվյալ շարժիչի համար հասանելի խարամների ցանկը.:

`doctl {{[d|databases]}} {{[o|options]}} {{[s|slugs]}} --engine {{pg|mysql|redis|mongodb}}`

- Ստացեք տվյալների բազայի տվյալ շարժիչի համար առկա տարբերակների ցանկը.:

`doctl {{[d|databases]}} {{[o|options]}} {{[v|versions]}} --engine {{pg|mysql|redis|mongodb}}`
