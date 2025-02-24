# git tag

> Cria, exibe, exclui ou verifica tags.
> Uma tag é uma referência estática para um commit.
> Mais informações: <https://git-scm.com/docs/git-tag>.

- Exibe todas as tags:

`git tag`

- Cria uma tag com o nome fornecido apontando para o commit atual:

`git tag {{nome_da_tag}}`

- Cria uma tag com o nome fornecido apontando para um determinado commit:

`git tag {{nome_da_tag}} {{commit}}`

- Cria uma tag anotada com a mensagem fornecida:

`git tag {{nome_da_tag}} {{[-m|--message]}} {{mensagem_da_tag}}`

- Exclui a tag com o nome fornecido:

`git tag {{[-d|--delete]}} {{nome_da_tag}}`

- Obtém tags atualizadas do remote:

`git fetch {{[-t|--tags]}}`

- Envia uma tag para o remote:

`git push origin tag {{nome_da_tag}}`

- Lista todas as tags cujos ancestrais incluem um determinado commit:

`git tag --contains {{commit}}`
