# docker ps

> Lista os containers Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/ps/>.

- Lista containers Docker em execução:

`docker ps`

- Lista todos containers Docker (em execução e parados):

`docker ps --all`

- Lista os últimos containers criados (incluí todos os estados):

`docker ps --latest`

- Filtra os containers que contém uma substring no seu nome:

`docker ps --filter="name={{nome}}"`

- Filtra todos os containers que possuem uma imagem antepassada:

`docker ps --filter "ancestor={{imagem}}:{{tag}}"`

- Filtra containers que tenha o código de saída:

`docker ps --all --filter="exited={{código}}"`

- Filtra containers por estado (criado, execução, removendo, pausado, finalizado e morto):

`docker ps --filter="status={{estado}}"`

- Filtra containers que contenham um volume específico ou montado em um caminho específico:

`docker ps --filter="volume={{caminho/para/diretório}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
