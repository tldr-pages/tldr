# git status

> Mostra as alterações nos arquivos em um repositório Git.
> Lista os arquivos alterados, adicionados e excluídos em comparação com o atual commit do checkout.
> Mais informações: <https://git-scm.com/docs/git-status>.

- Mostra arquivos alterados que ainda não foram adicionados para commit:

`git status`

- Fornece a saída em formato curto:

`git status --short`

- Mostra informação verbosa em alterações tanto na área de preparação e no diretório de trabalho:

`git status --verbose --verbose`

- Mostra informações da branch e de rastreamento:

`git status --branch`

- Mostra a saída em formato curto junto com as informações da branch:

`git status --short --branch`

- Mostra o número de entradas atualmente armazenadas:

`git status --show-stash`

- Não mostra arquivos não rastreados na saída:

`git status --untracked-files=no`
