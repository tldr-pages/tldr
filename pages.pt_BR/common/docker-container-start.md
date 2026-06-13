# docker container start

> Inicia um ou mais containers parados.
> Mais informações: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Inicia um container Docker:

`docker {{[start|container start]}} {{container}}`

- Inicia um container, atachando ao terminal os sinais `stdout` e `stderr` e outros sinais:

`docker {{[start|container start]}} {{[-a|--attach]}} {{container}}`

- Inicia um ou mais containers com ID separados por espaço:

`docker {{[start|container start]}} {{container1 container2 ...}}`

- Exibe a ajuda:

`docker {{[start|container start]}} --help`
