# docker compose

> Executa e gerencia multi-containers de aplicações Docker.
> Mais informações: <https://docs.docker.com/compose/reference/>.

- Lista todos os containers em execução:

`docker compose ps`

- Cria e inicia todos os containers em segundo plano usando um arquivo `docker-compose.yml` do seu diretório atual:

`docker compose up --detach`

- Inicia todos os containers. Se necessário, realiza um rebuild:

`docker compose up --build`

- Inicia todos os containers que estão usando um arquivo compose alternativo:

`docker compose --file {{caminho/para/arquivo}} up`

- Encerra todos os containers em execução:

`docker compose stop`

- Encerra e remove todos os containers, networks, imagens e volumes:

`docker compose down --rmi all --volumes`

- Segue os logs de todos os containers:

`docker compose logs --follow`

- Segue os logs de um container específico:

`docker compose logs --follow {{nome_container}}`
