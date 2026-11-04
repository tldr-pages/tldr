# docker compose down

> Para e remove contêineres, redes, imagens e volumes criados por `docker compose up`.
> Mais informações: <https://docs.docker.com/reference/cli/docker/compose/down/>.

- Para e remove todos os contêineres e redes:

`docker compose down`

- Para e remove contêineres, redes e todas as imagens usadas pelos serviços:

`docker compose down --rmi all`

- Para e remove contêineres, redes e apenas imagens sem uma tag personalizada:

`docker compose down --rmi local`

- Para e remove contêineres, redes e todos os volumes:

`docker compose down {{[-v|--volumes]}}`

- Para e remove tudo, incluindo contêineres órfãos:

`docker compose down --remove-orphans`

- Para e remove contêineres usando um arquivo Compose alternativo:

`docker compose {{[-f|--file]}} {{caminho/para/config}} down`

- Para e remove contêineres com um tempo limite personalizado em segundos:

`docker compose down {{[-t|--timeout]}} {{tempo_limite}}`

- Remove contêineres de serviços não definidos no arquivo Compose:

`docker compose down --remove-orphans {{[-v|--volumes]}}`
