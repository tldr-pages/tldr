# git rebase

> Reaplica os commits de uma branch sobre outra branch.
> Comumente usado para "mover" uma branch inteira para outra base, criando cópias dos commits na nova localização.
> Mais informações: <https://git-scm.com/docs/git-rebase>.

- Faz um rebase na branch atual sobre outra branch especificada:

`git rebase {{nova_branch_base}}`

- Inicia um rebase interativo, que permite os commits serem reordenados, omitidos, combinados ou modificados:

`git rebase -i {{branch_base_alvo_ou_hash_do_commit}}`

- Continua um rebase que foi interrompido por uma falha de mesclagem, após a edição de arquivos conflitantes:

`git rebase --continue`

- Continua um rebase que foi pausado devido a conflitos de mesclagem, ignorando o commit conflitante:

`git rebase --skip`

- Aborta um rebase em andamento (por exemplo, se ele foi interrompido por um conflito de mesclagem):

`git rebase --abort`

- Move parte da branch atual para uma nova base, fornecendo a base antiga para começar:

`git rebase --onto {{base_nova}} {{base_antiga}}`

- Reaplica os últimos 5 commits no local, parando para permitir que eles sejam reordenados, omitidos, combinados ou modificados:

`git rebase -i {{HEAD~5}}`

- Resolve automaticamente quaisquer conflitos favorecendo a versão da branch de trabalho (a palavra-chave `theirs` tem significado invertido nesse caso):

`git rebase -X theirs {{nome_da_branch}}`
