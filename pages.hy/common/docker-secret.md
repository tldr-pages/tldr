# դոկերի գաղտնիք

> Կառավարեք Docker swarm գաղտնիքները:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/secret/>:.

- Ստեղծեք նոր գաղտնիք `stdin`-ից.:

`{{command}} | docker secret create {{secret_name}} -`

- Ստեղծեք նոր գաղտնիք ֆայլից.:

`docker secret create {{secret_name}} {{path/to/file}}`

- Թվարկեք բոլոր գաղտնիքները.:

`docker secret ls`

- Ցուցադրել մանրամասն տեղեկատվություն մեկ կամ մի քանի գաղտնիքների մասին մարդու համար հարմար ձևաչափով.:

`docker secret inspect --pretty {{secret_name1 secret_name2 ...}}`

- Հեռացրեք մեկ կամ մի քանի գաղտնիք.:

`docker secret rm {{secret_name1 secret_name2 ...}}`
