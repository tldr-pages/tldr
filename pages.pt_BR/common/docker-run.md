# docker run

> Executa um comando em um novo container Docker.
> Mais informações: <https://docs.docker.com/reference/cli/docker/container/run/>.

- Executa um comando em um novo container de uma imagem tagueada:

`docker run {{imagem:tag}} {{comando}}`

- Executa um comando em um novo container em background e exibe o ID:

`docker run {{[-d|--detach]}} {{image}} {{command}}`

- Executa um comando em um novo container que será removido após a execução em um modo interativo e com um terminal TTY:

`docker run --rm {{[-it|--interactive --tty]}} {{image}} {{command}}`

- Executa um comando em um novo container com variáveis de ambiente:

`docker run {{[-e|--env]}} '{{variável}}={{valor}}' {{[-e|--env]}} {{variável}} {{imagem}} {{comando}}`

- Executa um comando em um novo container montando volumes nos caminhos específicos:

`docker run {{[-v|--volume]}} {{caminho/no/host_local}}:{{caminho/no/container}} {{imagem}} {{comando}}`

- Executa um comando em um novo container e abre as portas para acesso:

`docker run {{[-p|--publish]}} {{porta_do_host_local}}:{{porta_do_container}} {{imagem}} {{comando}}`

- Executa um comando em um novo container sobrescrevendo o entrypoint da imagem:

`docker run --entrypoint {{comando}} {{imagem}}`

- Executa um comando em um novo container conectando-o a rede:

`docker run --network {{rede}} {{imagem}}`
