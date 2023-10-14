# git checkout

> Faz checkout de uma ramificação ou caminhos para uma árvore de trabalho.
> Mais informações: <https://git-scm.com/docs/git-checkout>.

- Cria e muda para uma nova ramificação:

`git checkout -b {{nome_da_ramificação}}`

- Cria e muda para uma nova ramificação com base em uma referência específica (ramificação, remoto/ramificação, etiqueta são exemplos de referências válidas):

`git checkout -b {{nome_da_ramificação}} {{referência}}`

- Muda para uma ramificação local existente:

`git checkout {{nome_da_ramificação}}`

- Muda para uma ramificação previamente verificada:

`git checkout -`

- Muda para uma ramificação remota existente:

`git checkout --track {{nome_remoto}}/{{nome_da_ramificação}}`

- Descarta todas as alterações não preparadas no diretório atual (consulte `git reset` para mais comandos do tipo desfazer):

`git checkout .`

- Descarta alterações não preparadas em um determinado arquivo:

`git checkout {{caminho/para/arquivo}}`

- Substitui um arquivo no diretório atual com a versão com commit em uma determinada ramificação:

`git checkout {{nome_da_ramificação}} -- {{caminho/para/arquivo}}`
