# gh pr create

> Gerencia pull requests do GitHub.
> Mais informações: <https://cli.github.com/manual/gh_pr_create>.

- Cria um pull request interativamente:

`gh pr {{[new|create]}}`

- Cria um pull request, determinando o título e a descrição a partir das mensagens de commit da branch atual:

`gh pr {{[new|create]}} {{[-f|--fill]}}`

- Cria um pull request de rascunho:

`gh pr {{[new|create]}} {{[-d|--draft]}}`

- Cria um pull request especificando a branch base, o título e a descrição:

`gh pr {{[new|create]}} {{[-B|--base]}} {{branch_base}} {{[-t|--title]}} "{{título}}" {{[-b|--body]}} "{{descrição}}"`

- Começa a abrir um pull request no navegador padrão:

`gh pr {{[new|create]}} {{[-w|--web]}}`
