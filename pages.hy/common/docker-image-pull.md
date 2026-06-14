# docker պատկերի ձգում

> Ներբեռնեք Docker պատկերները գրանցամատյանից:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/image/pull/>:.

- Ներբեռնեք կոնկրետ Docker պատկեր.:

`docker {{[pull|image pull]}} {{image}}:{{tag}}`

- Ներբեռնեք որոշակի Docker պատկեր հանգիստ ռեժիմով.:

`docker {{[pull|image pull]}} {{[-q|--quiet]}} {{image}}:{{tag}}`

- Ներբեռնեք որոշակի Docker պատկերի բոլոր պիտակները.:

`docker {{[pull|image pull]}} {{[-a|--all-tags]}} {{image}}`

- Ներբեռնեք Docker պատկերները որոշակի հարթակի համար.:

`docker {{[pull|image pull]}} --platform {{linux/amd64}} {{image}}:{{tag}}`

- Ցուցադրել օգնությունը.:

`docker {{[pull|image pull]}} --help`
