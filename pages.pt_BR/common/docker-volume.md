# docker volume

> Gerenciar volumes do Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/volume/>.

- Cria um volume:

`docker volume create {{nome_do_volume}}`

- Cria um volume com um rótulo específico:

`docker volume create --label {{rótulo}} {{nome_do_volume}}`

- Cria um volume `tmpfs` com tamanho de 100 MiB e uid 1000:

`docker volume create --opt {{type}}={{tmpfs}} --opt {{device}}={{tmpfs}} --opt {{o}}={{size=100m,uid=1000}} {{nome_do_volume}}`

- Lista todos os volumes:

`docker volume ls`

- Remove um volume:

`docker volume rm {{nome_do_volume}}`

- Exibe informações sobre um volume:

`docker volume inspect {{nome_do_volume}}`

- Remove todos os volumes locais não utilizados:

`docker volume prune`

- Exibe ajuda para um subcomando:

`docker volume {{subcomando}} --help`
