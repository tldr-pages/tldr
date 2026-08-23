# docker compose start

> Inicia contêineres existentes dos serviços.
> Mais informações: <https://docs.docker.com/reference/cli/docker/compose/start/>.

- Inicia os contêineres existentes de todos os serviços:

`docker compose start`

- Inicia os contêineres existentes de um ou mais serviços:

`docker compose start {{serviço1 serviço2 ...}}`

- Simula a inicialização dos contêineres existentes:

`docker compose start --dry-run`

- Inicia os contêineres existentes e aguarda os serviços estarem em execução ou saudáveis:

`docker compose start --wait`

- Inicia os contêineres existentes e aguarda por até um número especificado de segundos:

`docker compose start --wait --wait-timeout {{segundos}}`
