# docker exec

> Executar um comando em um contêiner Docker em execução.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Entrar em uma sessão de shell interativa em um contêiner em execução:

`docker exec --interactive --tty {{nome_do_contêiner}} {{/bin/bash}}`

- Executar um comando em segundo plano (detached) em um contêiner em execução:

`docker exec --detach {{nome_do_contêiner}} {{comando}}`

- Selecionar o diretório de trabalho para a execução de um determinado comando:

`docker exec --interactive --tty --workdir {{caminho/para/diretório}} {{nome_do_contêiner}} {{comando}}`

- Executar um comando em segundo plano em um contêiner existente, mas manter o `stdin` aberto:

`docker exec --interactive --detach {{nome_do_contêiner}} {{comando}}`

- Definir uma variável de ambiente em uma sessão Bash em execução:

`docker exec --interactive --tty --env {{nome_da_variável}}={{valor}} {{nome_do_contêiner}} {{/bin/bash}}`

- Executar um comando como um usuário específico:

`docker exec --user {{usuário}} {{nome_do_contêiner}} {{comando}}`
