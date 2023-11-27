# git init

> Inicializa um novo repositório Git local.
> Mais informações: <https://git-scm.com/docs/git-init>.

- Inicializa um novo repositório local:

`git init`

- Inicializa um repositório com o nome especificado para a branch inicial:

`git init --initial-branch={{nome_da_branch}}`

- Inicializa um repositório usando SHA256 para os hashes de objeto (requer Git versão 2.29+):

`git init --object-format={{sha256}}`

- Inicializa um repositório barebones, adequado para usar como um remoto via ssh:

`git init --bare`
