# docker ps

> Lista os contêineres Docker.
> Mais informações: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Lista contêineres Docker em execução:

`docker ps`

- Lista todos contêineres Docker (em execução e parados):

`docker ps {{[-a|--all]}}`

- Lista os últimos contêineres criados (inclui todos os estados):

`docker ps {{[-l|--latest]}}`

- Filtra os contêineres que contêm uma substring no seu nome:

`docker ps {{[-f|--filter]}} "name={{nome}}"`

- Filtra todos os contêineres que compartilham uma determinada imagem com um antepassado:

`docker ps {{[-f|--filter]}} "ancestor={{imagem}}:{{tag}}"`

- Filtra contêineres que tenham o código de saída:

`docker ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{código}}"`

- Filtra contêineres por estado (created, running, removing, paused, exited e dead):

`docker ps {{[-f|--filter]}} "status={{estado}}"`

- Filtra contêineres que montem um volume específico ou tenham um volume montado em um caminho específico:

`docker ps {{[-f|--filter]}} "volume={{caminho/para/diretório}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
