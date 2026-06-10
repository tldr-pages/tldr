# դոկեր ցանց

> Ստեղծեք և կառավարեք Docker ցանցերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/network/>:.

- Թվարկեք բոլոր հասանելի և կազմաձևված ցանցերը Docker daemon-ում.:

`docker network ls`

- Ստեղծեք օգտագործողի կողմից սահմանված ցանց.:

`docker network create {{[-d|--driver]}} {{driver_name}} {{network_name}}`

- Ցուցադրել մանրամասն տեղեկատվություն մեկ կամ մի քանի ցանցերի մասին.:

`docker network inspect {{network_name1 network_name2 ...}}`

- Միացրեք կոնտեյները ցանցին՝ օգտագործելով անուն կամ ID.:

`docker network connect {{network_name}} {{container_name|id}}`

- Անջատեք կոնտեյները ցանցից.:

`docker network disconnect {{network_name}} {{container_name|id}}`

- Հեռացրեք բոլոր չօգտագործված (ոչ մի կոնտեյների կողմից նշված) ցանցերը.:

`docker network prune`

- Հեռացրեք մեկ կամ մի քանի չօգտագործված ցանցեր.:

`docker network rm {{network_name1 network_name2 ...}}`
