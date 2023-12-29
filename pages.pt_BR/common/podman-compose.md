# podman-compose

> Executar e gerenciar definição de contêineres Compose Specification.
> Mais informações: <https://github.com/containers/podman-compose>.

- Lista todos os contêineres em execução:

`podman-compose ps`

- Cria e inicia todos os contêineres em segundo plano usando um arquivo `docker-compose.yml` local:

`podman-compose up -d`

- Inicia todos os contêineres, fazendo o build se necessário:

`podman-compose up --build`

- Inicia todos os contêineres usando um arquivo de composição alternativo:

`podman-compose {{caminho/para/arquivo}} up`

- Para todos os contêineres em execução:

`podman-compose stop`

- Remove todos os contêineres, redes e volumes:

`podman-compose down --volumes`

- Acompanha logs de um contêiner (omite todos os nomes de contêineres):

`podman-compose logs --follow {{nome_do_contêiner}}`

- Executa um comando único em um serviço sem mapear portas:

`podman-compose run {{nome_do_serviço}} {{comando}}`
