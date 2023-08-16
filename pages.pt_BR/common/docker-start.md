# docker start

> Inicia um ou mais containers parados.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/start/>.

- Exibe a ajuda:

`docker start`

- Inicia um container docker:

`docker start {{container}}`

- Inicia um container, atachando ao terminal os sinais `stdout` e `stderr` e outros sinais:

`docker start --attach {{container}}`

- Inicia um ou mais containers com ID separados por espaço:

`docker start {{container1 container2 ...}}`
