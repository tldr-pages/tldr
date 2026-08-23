# docker compose logs

> Visualiza a saída dos contêineres de uma aplicação Docker Compose.
> Mais informações: <https://docs.docker.com/reference/cli/docker/compose/logs/>.

- Visualiza os registros (logs) de todos os serviços:

`docker compose logs`

- Visualiza os registros de um serviço específico:

`docker compose logs {{nome_do_serviço}}`

- Visualiza os registros e acompanha novas saídas (como `tail --follow`):

`docker compose logs {{[-f|--follow]}}`

- Visualiza os registros com timestamps:

`docker compose logs {{[-t|--timestamps]}}`

- Visualiza apenas as últimas `n` linhas de registros de cada contêiner:

`docker compose logs {{[-n|--tail]}} {{n}}`

- Visualiza os registros a partir de um horário específico:

`docker compose logs --since {{timestamp}}`

- Visualiza os registros até um horário específico:

`docker compose logs --until {{timestamp}}`

- Visualiza os registros de vários serviços específicos:

`docker compose logs {{serviço1 serviço2 ...}}`
