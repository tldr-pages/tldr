# git checkout

> Faz checkout de uma branch ou caminhos para uma árvore de trabalho.
> Mais informações: <https://git-scm.com/docs/git-checkout>.

- Cria e muda para uma nova branch:

`git checkout -b {{nome_da_branch}}`

- Cria e muda para uma nova branch com base em uma referência específica (branch, remoto/branch, etiqueta são exemplos de referências válidas):

`git checkout -b {{nome_da_branch}} {{referência}}`

- Muda para uma branch local existente:

`git checkout {{nome_da_branch}}`

- Muda para uma branch previamente verificada:

`git checkout -`

- Muda para uma branch remota existente:

`git checkout --track {{nome_remoto}}/{{nome_da_branch}}`

- Descarta todas as alterações não preparadas no diretório atual (consulte `git reset` para mais comandos do tipo desfazer):

`git checkout .`

- Descarta alterações não preparadas em um determinado arquivo:

`git checkout {{caminho/para/arquivo}}`

- Substitui um arquivo no diretório atual com a versão com commit em uma determinada branch:

`git checkout {{nome_da_branch}} -- {{caminho/para/arquivo}}`
