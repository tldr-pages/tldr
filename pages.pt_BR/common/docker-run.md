# docker run

> Executa um comando em um novo container Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/run/>.

- Executa um comando em um novo container de uma imagem tagueada:

`docker run {{imagem:tag}} {{comando}}`

- Executa um comando em um novo container em background e exibe o ID:

`docker run -d {{image}} {{command}}`

- Executa um comando em um novo container que será removido após a execução em um modo interativo e com um terminal TTY:

`docker run --rm -it {{image}} {{command}}`

- Executa um comando em um novo container com variáveis de ambiente:

`docker run -e '{{variável}}={{valor}}' -e {{variável}} {{imagem}} {{comando}}`

- Executa um comando em um novo container montando volumes nos caminhos específicos:

`docker run -v {{caminho/no/host_local}}:{{caminho/no/container}} {{imagem}} {{comando}}`

- Executa um comando em um novo container e abre as portas para acesso:

`docker run -p {{porta_do_host_local}}:{{porta_do_container}} {{imagem}} {{comando}}`
