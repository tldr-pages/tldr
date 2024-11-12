# docker ps

> Lista os contêineres Docker.
> Mais informações: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Lista contêineres Docker em execução:

`docker ps`

- Lista todos contêineres Docker (em execução e parados):

`docker ps --all`

- Lista os últimos contêineres criados (inclui todos os estados):

`docker ps --latest`

- Filtra os contêineres que contêm uma substring no seu nome:

`docker ps --filter "name={{nome}}"`

- Filtra todos os contêineres que compartilham uma determinada imagem com um antepassado:

`docker ps --filter "ancestor={{imagem}}:{{tag}}"`

- Filtra contêineres que tenham o código de saída:

`docker ps --all --filter "exited={{código}}"`

- Filtra contêineres por estado (created, running, removing, paused, exited e dead):

`docker ps --filter "status={{estado}}"`

- Filtra contêineres que montem um volume específico ou tenham um volume montado em um caminho específico:

`docker ps --filter "volume={{caminho/para/diretório}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
