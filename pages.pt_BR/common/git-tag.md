# git tag

> Cria, exibe, exclui ou verifica tags.
> Uma tag é uma referência estática para um commit específico.
> Mais informações: <https://git-scm.com/docs/git-tag>.

- Exibe todas as tags:

`git tag`

- Crie uma tag com o nome fornecido apontando para o commit atual:

`git tag {{nome_da_tag}}`

- Crie uma tag com o nome fornecido apontando para um determinado commit:

`git tag {{nome_da_tag}} {{commit}}`

- Cria uma tag anotada com a mensagem fornecida:

`git tag {{nome_da_tag}} -m {{mensagem_da_tag}}`

- Exclui a tag com o nome fornecido:

`git tag -d {{nome_da_tag}}`

- Obtenha tags atualizadas do upstream:

`git fetch --tags`

- Liste todas as tags cujos ancestrais incluem um determinado commit:

`git tag --contains {{commit}}`
