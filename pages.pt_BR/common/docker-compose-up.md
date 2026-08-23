# docker compose up

> Inicia e executa os serviços Docker definidos em um arquivo Compose.
> Mais informações: <https://docs.docker.com/reference/cli/docker/compose/up/>.

- Inicia todos os serviços definidos no arquivo docker-compose:

`docker compose up`

- Inicia os serviços em segundo plano (modo destacado):

`docker compose up {{[-d|--detach]}}`

- Inicia os serviços e reconstrói as imagens antes de iniciar:

`docker compose up --build`

- Inicia apenas serviços específicos:

`docker compose up {{serviço1 serviço2 ...}}`

- Inicia os serviços com um arquivo compose personalizado:

`docker compose {{[-f|--file]}} {{caminho/para/config}} up`

- Inicia os serviços e remove contêineres órfãos:

`docker compose up --remove-orphans`

- Inicia os serviços com instâncias em escala:

`docker compose up --scale {{serviço}}={{contagem}}`

- Inicia os serviços e mostra os registros com timestamps:

`docker compose up --timestamps`
