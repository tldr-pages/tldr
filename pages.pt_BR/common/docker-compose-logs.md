# docker compose logs

> Exibe a saída dos contêineres de uma aplicação Docker Compose.
> Mais informações: <https://docs.docker.com/reference/cli/docker/compose/logs/>.

- Exibe os registros (logs) de todos os serviços:

`docker compose logs`

- Exibe os registros de um serviço específico:

`docker compose logs {{nome_do_serviço}}`

- Exibe os registros e acompanha novas saídas (como `tail --follow`):

`docker compose logs {{[-f|--follow]}}`

- Exibe os registros com timestamps:

`docker compose logs {{[-t|--timestamps]}}`

- Exibe apenas as últimas `n` linhas de registros de cada contêiner:

`docker compose logs {{[-n|--tail]}} {{n}}`

- Exibe os registros a partir de um horário específico:

`docker compose logs --since {{timestamp}}`

- Exibe os registros até um horário específico:

`docker compose logs --until {{timestamp}}`

- Exibe os registros de vários serviços específicos:

`docker compose logs {{serviço1 serviço2 ...}}`
