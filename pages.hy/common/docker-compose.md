# դոկեր գրել

> Գործարկել և կառավարել բազմաբեռնարկղային Docker հավելվածները:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/compose/>:.

- Թվարկեք բոլոր ընթացիկ բեռնարկղերը.:

`docker compose ps`

- Ստեղծեք և գործարկեք բոլոր բեռնարկղերը հետին պլանում՝ օգտագործելով `docker-compose.yml` ֆայլը ընթացիկ գրացուցակից:

`docker compose up {{[-d|--detach]}}`

- Սկսեք բոլոր բեռնարկղերը, անհրաժեշտության դեպքում վերակառուցեք.:

`docker compose up --build`

- Սկսեք բոլոր բեռնարկղերը՝ նշելով նախագծի անվանումը և օգտագործելով այլընտրանքային կազմման ֆայլ.:

`docker compose {{[-p|--project-name]}} {{project_name}} {{[-f|--file]}} {{path/to/file}} up`

- Դադարեցրեք բոլոր հոսող բեռնարկղերը.:

`docker compose stop`

- Դադարեցրեք և հեռացրեք բոլոր բեռնարկղերը, ցանցերը, պատկերները և ծավալները.:

`docker compose down --rmi all {{[-v|--volumes]}}`

- Հետևեք բոլոր բեռնարկղերի տեղեկամատյաններին.:

`docker compose logs {{[-f|--follow]}}`

- Հետևեք տեղեկամատյաններին որոշակի կոնտեյների համար.:

`docker compose logs {{[-f|--follow]}} {{container_name}}`
