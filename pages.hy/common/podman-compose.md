# podman-շարադրել

> Գործարկել և կառավարել Compose Specification կոնտեյների սահմանումը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/containers/podman-compose>:.

- Թվարկեք բոլոր ընթացիկ բեռնարկղերը.:

`podman-compose ps`

- Ստեղծեք և գործարկեք բոլոր բեռնարկղերը հետին պլանում՝ օգտագործելով տեղական `docker-compose.yml`:

`podman-compose up {{[-d|--detach]}}`

- Սկսեք բոլոր բեռնարկղերը, անհրաժեշտության դեպքում կառուցեք.:

`podman-compose up --build`

- Սկսեք բոլոր բեռնարկղերը՝ օգտագործելով այլընտրանքային կազմման ֆայլ.:

`podman-compose {{[-f|--file]}} {{path/to/file.yaml}} up`

- Դադարեցրեք բոլոր հոսող բեռնարկղերը.:

`podman-compose stop`

- Հեռացրեք բոլոր բեռնարկղերը, ցանցերը և ծավալները.:

`podman-compose down {{[-v|--volumes]}}`

- Հետևեք կոնտեյների տեղեկամատյաններին (բաց թողեք բոլոր բեռնարկղերի անունները).:

`podman-compose logs {{[-f|--follow]}} {{container_name}}`

- Գործարկեք մեկանգամյա հրաման ծառայությունում, որտեղ նավահանգիստներ չկան քարտեզագրված.:

`podman-compose run {{service_name}} {{command}}`
