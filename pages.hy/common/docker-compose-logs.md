# docker կազմման տեղեկամատյաններ

> Դիտեք բեռնարկղերից ստացված արդյունքները Docker Compose հավելվածում:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/compose/logs/>:.

- Դիտեք տեղեկամատյանները բոլոր ծառայությունների համար.:

`docker compose logs`

- Դիտեք տեղեկամատյանները որոշակի ծառայության համար.:

`docker compose logs {{service_name}}`

- Դիտեք տեղեկամատյանները և հետևեք նոր արդյունքներին (ինչպես `tail --follow`):

`docker compose logs {{[-f|--follow]}}`

- Դիտեք տեղեկամատյանները ժամանակային դրոշմանիշներով.:

`docker compose logs {{[-t|--timestamps]}}`

- Դիտեք միայն տեղեկամատյանների վերջին `n` տողերը յուրաքանչյուր կոնտեյների համար.:

`docker compose logs {{[-n|--tail]}} {{n}}`

- Դիտեք տեղեկամատյանները որոշակի ժամանակից սկսած.:

`docker compose logs --since {{timestamp}}`

- Դիտեք տեղեկամատյանները մինչև որոշակի ժամանակ.:

`docker compose logs --until {{timestamp}}`

- Դիտեք բազմաթիվ հատուկ ծառայությունների տեղեկամատյանները.:

`docker compose logs {{service1 service2 ...}}`
