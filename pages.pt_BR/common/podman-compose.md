# podman-compose

> Executar e gerenciar definição de contêineres Compose Specification.
> Mais informações: <https://github.com/containers/podman-compose>.

- Listar todos os contêineres em execução:

`podman-compose ps`

- Criar e iniciar todos os contêineres em segundo plano usando um arquivo `docker-compose.yml` local:

`podman-compose up -d`

- Iniciar todos os contêineres, fazendo o build se necessário:

`podman-compose up --build`

- Iniciar todos os contêineres usando um arquivo de composição alternativo:

`podman-compose {{caminho/para/arquivo}} up`

- Parar todos os contêineres em execução:

`podman-compose stop`

- Remover todos os contêineres, redes e volumes:

`podman-compose down --volumes`

- Acompanhar logs de um contêiner (omitir todos os nomes de contêineres):

`podman-compose logs --follow {{nome_do_contêiner}}`

- Executar um comando único em um serviço sem mapear portas:

`podman-compose run {{nome_do_serviço}} {{comando}}`
