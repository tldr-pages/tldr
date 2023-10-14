# git branch

> Comando principal do Git para trabalhar com ramificações.
> Mais informações: <https://git-scm.com/docs/git-branch>.

- Lista todas as ramificações (locais e remotas; a ramificação atual é destacada por `*`):

`git branch --all`

- Lista quais ramificações incluem um commit específico do Git em seu histórico:

`git branch --all --contains {{hash_do_commit}}`

- Mostra o nome da ramificação atual:

`git branch --show-current`

- Cria uma nova ramificação baseada no commit atual:

`git branch {{name_da_ramificação}}`

-Crua uma nova ramificação baseada em um commit específico:

`git branch {{nome_da_ramificação}} {{hash_do_commit}}`

- Renomeia uma ramificação (não precisa fazer checkout para isso):

`git branch -m {{antigo_nome_da_ramificação}} {{novo_nome_da_ramificação}}`

- Exclui a ramificação local (não precisa fazer checkout para isso):

`git branch -d {{name_da_branch}}`

- Exclui uma ramificação remota:

`git push {{nome_remoto}} --delete {{name_da_ramificação_remota}}`
