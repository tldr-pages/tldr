# git branch

> Comando principal do Git para trabalhar com branches.
> Mais informações: <https://git-scm.com/docs/git-branch>.

- Lista todas as branches (locais e remotas; a branch atual é destacada por `*`):

`git branch --all`

- Lista quais branches incluem um commit específico do Git em seu histórico:

`git branch --all --contains {{hash_do_commit}}`

- Mostra o nome da branch atual:

`git branch --show-current`

- Cria uma nova branch baseada no commit atual:

`git branch {{nome_da_branch}}`

- Crua uma nova branch baseada em um commit específico:

`git branch {{nome_da_branch}} {{hash_do_commit}}`

- Renomeia uma branch (não precisa fazer checkout para isso):

`git branch -m {{antigo_nome_da_branch}} {{novo_nome_da_branch}}`

- Exclui a branch local (não precisa fazer checkout para isso):

`git branch -d {{nome_da_branch}}`

- Exclui uma branch remota:

`git push {{nome_remoto}} --delete {{nome_da_branch_remota}}`
