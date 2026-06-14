# դոկերի ծավալ

> Կառավարեք Docker ծավալները:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/volume/>:.

- Ստեղծեք հատոր.:

`docker volume create {{volume_name}}`

- Ստեղծեք հատոր հատուկ պիտակով.:

`docker volume create --label {{label}} {{volume_name}}`

- Ստեղծեք `tmpfs` հատոր 100 ՄԲ չափով և 1000 Uid:

`docker volume create {{[-o|--opt]}} {{type}}={{tmpfs}} {{[-o|--opt]}} {{device}}={{tmpfs}} {{[-o|--opt]}} {{o}}={{size=100m,uid=1000}} {{volume_name}}`

- Թվարկեք բոլոր հատորները.:

`docker volume ls`

- Հեռացնել ծավալը՝:

`docker volume rm {{volume_name}}`

- Ցուցադրել տեղեկատվություն ծավալի մասին.:

`docker volume inspect {{volume_name}}`

- Հեռացրեք բոլոր չօգտագործված տեղական ծավալները.:

`docker volume prune`

- Ցուցադրել օգնություն ենթահրամանի համար.:

`docker volume {{subcommand}} --help`
