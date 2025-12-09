# docker logs

> Exibe os logs dos containers.
> Mais informações: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Exibe logs de um container:

`docker logs {{nome_do_container}}`

- Exibe logs de um container e segue exibindo:

`docker logs {{[-f|--follow]}} {{nome_do_container}}`

- Exibe as últimas 5 linhas:

`docker logs {{nome_do_container}} {{[-n|--tail]}} {{5}}`

- Exibe logs e adiciona a informação de hora ao log:

`docker logs {{[-t|--timestamps]}} {{nome_do_container}}`

- Exibe logs até um certo ponto no tempo de execução do container (por exemplo: 23m, 10s, 2013-01-02T13:23:37):

`docker logs {{nome_do_container}} --until {{tempo}}`
