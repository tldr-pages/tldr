# docker stats

> Exibe estatísticas dinâmicas de uso de recursos dos containers.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Exibe estatísticas atualizadas de todos os containers em execução:

`docker stats`

- Exibe estatísticas atualizadas de uma lista separada por espaço dos containers:

`docker stats {{nome_do_container}}`

- Altera o formato das colunas para exibir o uso da CPU em porcentagem:

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- Exibe estatísticas para todos os containers (tanto em execução como parados):

`docker stats --all`

- Desabilita estatísticas atualizadas e só exibe o status naquele momento:

`docker stats --no-stream`
