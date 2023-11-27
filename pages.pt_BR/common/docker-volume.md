# docker volume

> Gerenciar volumes do Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/volume/>.

- Criar um volume:

`docker volume create {{nome_do_volume}}`

- Criar um volume com um rótulo específico:

`docker volume create --label {{rótulo}} {{nome_do_volume}}`

- Criar um volume `tmpfs` com tamanho de 100 MiB e uid 1000:

`docker volume create --opt {{type}}={{tmpfs}} --opt {{device}}={{tmpfs}} --opt {{o}}={{size=100m,uid=1000}} {{nome_do_volume}}`

- Listar todos os volumes:

`docker volume ls`

- Remover um volume:

`docker volume rm {{nome_do_volume}}`

- Exibir informações sobre um volume:

`docker volume inspect {{nome_do_volume}}`

- Remover todos os volumes locais não utilizados:

`docker volume prune`

- Exibir ajuda para um subcomando:

`docker volume {{subcomando}} --help`
