# docker logs

> Exibe os logs dos containers.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/logs>.

- Exibe logs de um container:

`docker logs {{nome_do_container}}`

- Exibe logs de um container e segue exibindo:

`docker logs -f {{nome_do_container}}`

- Exibe as últimas 5 linhas:

`docker logs {{nome_do_container}} --tail {{5}}`

- Exibe logs e adiciona a informação de hora ao log:

`docker logs -t {{nome_do_container}}`

- Exibe logs até um certo ponto no tempo de execução do container (por exemplo: 23m, 10s, 2013-01-02T13:23:37):

`docker logs {{nome_do_container}} --until {{tempo}}`
