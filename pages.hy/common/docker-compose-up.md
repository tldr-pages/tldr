# docker կազմեք

> Սկսեք և գործարկեք Docker ծառայությունները, որոնք սահմանված են Compose ֆայլում:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/compose/up/>:.

- Սկսեք բոլոր ծառայությունները, որոնք սահմանված են docker-compose ֆայլում.:

`docker compose up`

- Ծառայությունների մեկնարկը հետին պլանում (անջատված ռեժիմ).:

`docker compose up {{[-d|--detach]}}`

- Սկսեք ծառայությունները և վերակառուցեք պատկերները նախքան սկսելը.:

`docker compose up --build`

- Սկսեք միայն հատուկ ծառայություններ.:

`docker compose up {{service1 service2 ...}}`

- Ծառայություններ սկսել մաքսային կազմման ֆայլով.:

`docker compose {{[-f|--file]}} {{path/to/config}} up`

- Սկսեք ծառայությունները և հեռացրեք որբացած տարաները.:

`docker compose up --remove-orphans`

- Սկսեք ծառայությունները մասշտաբային օրինակներով.:

`docker compose up --scale {{service}}={{count}}`

- Սկսեք ծառայությունները և ցուցադրեք տեղեկամատյանները ժամանակային դրոշմանիշներով.:

`docker compose up --timestamps`
