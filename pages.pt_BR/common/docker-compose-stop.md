# docker compose stop

> Para contêineres em execução sem removê-los.
> Mais informações: <https://docs.docker.com/reference/cli/docker/compose/stop>.

- Para todos os serviços em execução:

`docker compose stop`

- Para serviços específicos:

`docker compose stop {{serviço_1 serviço_2 ...}}`

- Para com um tempo limite de desligamento personalizado em segundos:

`docker compose stop {{[-t|--timeout]}} {{segundos}}`

- Para os serviços definidos em um arquivo compose específico:

`docker compose {{[-f|--file]}} {{caminho/para/arquivo_compose}} stop`

- Execução simulada (mostra as operações sem executá-las):

`docker compose stop --dry-run`

- Para serviços específicos com um tempo limite personalizado:

`docker compose stop {{[-t|--timeout]}} {{segundos}} {{serviço_1 serviço_2 ...}}`
