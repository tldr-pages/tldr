# docker secret

> Gerenciar segredos do Docker swarm.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/secret/>.

- Criar um novo segredo a partir de `stdin`:

`{{comando}} | docker secret create {{nome_do_segredo}} -`

- Criar um novo segredo a partir de um arquivo:

`docker secret create {{nome_do_segredo}} {{caminho/para/arquivo}}`

- Listar todos os segredos:

`docker secret ls`

- Exibir informações detalhadas sobre um ou vários segredos em um formato amigável ao usuário:

`docker secret inspect --pretty {{nome_do_segredo1 nome_do_segredo2 ...}}`

- Remover um ou mais segredos:

`docker secret rm {{nome_do_segredo1 nome_do_segredo2 ...}}`
