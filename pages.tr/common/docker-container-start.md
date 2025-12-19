# docker start

> Bir veya daha fazla durmuş konteyneri başlar.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Yardım göster:

`docker start`

- Bir Docker konteynerini başlat:

`docker start {{konteyner}}`

- Bir konteyneri, ona `stdout` ile `stderr`'i ekleyerek ve sinyaller göndererek başlat:

`docker start {{[-a|--attach]}} {{konteyner}}`

- Bir veya daha fazla boşlukla ayrılarak belirtilmiş konteynerleri başlar:

`docker start {{konteyner1 konteyner2 ...}}`
