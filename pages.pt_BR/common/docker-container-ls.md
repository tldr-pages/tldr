# docker container ls

> Lista os contêineres Docker.
> Mais informações: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Lista contêineres Docker em execução:

`docker {{[ps|container ls]}}`

- Lista todos contêineres Docker (em execução e parados):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Lista os últimos contêineres criados (inclui todos os estados):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Filtra os contêineres que contêm uma substring no seu nome:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{nome}}"`

- Filtra todos os contêineres que compartilham uma determinada imagem com um antepassado:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{imagem}}:{{tag}}"`

- Filtra contêineres que tenham o código de saída:

`docker {{[ps|container ls]}} {{[-a|--all]}} {{[-f|--filter]}} "exited={{código}}"`

- Filtra contêineres por estado (created, running, removing, paused, exited e dead):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{estado}}"`

- Filtra contêineres que montem um volume específico ou tenham um volume montado em um caminho específico:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{caminho/para/diretório}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
