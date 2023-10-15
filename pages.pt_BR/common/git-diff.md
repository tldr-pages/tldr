# git diff

> Mostra alterações nos arquivos rastreados.
> Mais informações: <https://git-scm.com/docs/git-diff>.

- Mostra as alterações não preparadas e sem commit:

`git diff`

- Mostra todas as alterações sem commit (incluindo as preparadas):

`git diff HEAD`

- Mostra apenas as alterações preparadas (adicionadas, mas ainda sem commit):

`git diff --staged`

- Mostra as alterações de todos os commits desde uma determinada data/hora (uma expressão de data, por exemplo, "1 week 2 days" ou uma data ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Mostra apenas os nomes dos arquivos alterados desde um determinado commit:

`git diff --name-only {{commit}}`

- Emite um resumo das criações de arquivos, renomeações e alterações de modo desde um determinado commit:

`git diff --summary {{commit}}`

- Compara um único arquivo entre duas branches ou commits:

`git diff {{branch_1}}..{{branch_2}} [--] {{caminho/para/arquivo}}`

- Compara diferentes arquivos da branch atual com outra branch:

`git diff {{branch}}:{{caminho/para/arquivo2}} {{caminho/para/arquivo}}`
