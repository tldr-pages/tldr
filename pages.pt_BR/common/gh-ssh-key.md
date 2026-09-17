# gh ssh-key

> Gerencia chaves SSH do GitHub.
> Mais informações: <https://cli.github.com/manual/gh_ssh-key>.

- Lista as chaves SSH do usuário autenticado no momento:

`gh ssh-key {{[ls|list]}}`

- Adiciona uma chave SSH à conta do usuário autenticado no momento:

`gh ssh-key add {{caminho/para/chave.pub}}`

- Adiciona uma chave SSH à conta do usuário autenticado no momento com um título específico:

`gh ssh-key add {{[-t|--title]}} {{título}} {{caminho/para/chave.pub}}`

- Mostra ajuda:

`gh ssh-key`
