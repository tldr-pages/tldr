# docker buildx create

> Cria uma nova instância de builder.
> Mais informações: <https://docs.docker.com/reference/cli/docker/buildx/create/>.

- Cria uma nova instância de builder usando o contexto Docker padrão:

`docker buildx create`

- Cria uma nova instância de builder com um nome específico:

`docker buildx create --name {{nome_do_builder}}`

- Cria uma nova instância de builder e a define imediatamente como o builder ativo atual:

`docker buildx create --name {{nome_do_builder}} --use`

- Cria uma nova instância de builder usando um driver específico (padrão: `docker`):

`docker buildx create --driver {{docker-container|kubernetes|remote|...}}`

- Cria uma nova instância de builder com plataformas suportadas específicas:

`docker buildx create --platform {{linux/amd64,linux/arm64,...}}`

- Adiciona um novo nó a um builder existente:

`docker buildx create --name {{nome_do_builder}} --append {{contexto|endpoint}}`

- Cria uma nova instância de builder com flags específicas do daemon BuildKit:

`docker buildx create --buildkitd-flags "{{--debug --debugaddr 0.0.0.0:6666}}"`

- Cria uma nova instância de builder e a inicia imediatamente:

`docker buildx create --name {{nome_do_builder}} --bootstrap`
