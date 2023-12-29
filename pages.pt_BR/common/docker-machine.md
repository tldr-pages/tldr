# docker-machine

> Criar e gerenciar máquinas que executam o Docker.
> Mais informações: <https://docs.docker.com/machine/reference/>.

- Lista as máquinas Docker em execução no momento:

`docker-machine ls`

- Cria uma nova máquina Docker com um nome específico:

`docker-machine create {{nome}}`

- Obtém o status de uma máquina:

`docker-machine status {{nome}}`

- Inicia uma máquina:

`docker-machine start {{nome}}`

- Para uma máquina:

`docker-machine stop {{nome}}`

- Inspeciona informações sobre uma máquina:

`docker-machine inspect {{nome}}`
