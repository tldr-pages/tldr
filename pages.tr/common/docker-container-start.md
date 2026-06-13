# docker container start

> Bir veya daha fazla durmuş konteyneri başlar.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Bir Docker konteynerini başlat:

`docker {{[start|container start]}} {{konteyner}}`

- Bir konteyneri, ona `stdout` ile `stderr`'i ekleyerek ve sinyaller göndererek başlat:

`docker {{[start|container start]}} {{[-a|--attach]}} {{konteyner}}`

- Bir veya daha fazla boşlukla ayrılarak belirtilmiş konteynerleri başlar:

`docker {{[start|container start]}} {{konteyner1 konteyner2 ...}}`

- Yardım göster:

`docker {{[start|container start]}} --help`
