# docker-machine

> Criar e gerenciar máquinas que executam o Docker.
> Mais informações: <https://docs.docker.com/machine/reference/>.

- Listar as máquinas Docker em execução no momento:

`docker-machine ls`

- Criar uma nova máquina Docker com um nome específico:

`docker-machine create {{nome}}`

- Obter o status de uma máquina:

`docker-machine status {{nome}}`

- Iniciar uma máquina:

`docker-machine start {{nome}}`

- Parar uma máquina:

`docker-machine stop {{nome}}`

- Inspecionar informações sobre uma máquina:

`docker-machine inspect {{nome}}`
