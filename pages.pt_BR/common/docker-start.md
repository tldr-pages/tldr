# docker start

> Inicia um ou mais containers parados.
> Mais informações: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Exibe a ajuda:

`docker start`

- Inicia um container Docker:

`docker start {{container}}`

- Inicia um container, atachando ao terminal os sinais `stdout` e `stderr` e outros sinais:

`docker start {{[-a|--attach]}} {{container}}`

- Inicia um ou mais containers com ID separados por espaço:

`docker start {{container1 container2 ...}}`
