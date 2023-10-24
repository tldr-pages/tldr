# git reset

> Desfaz os commits ou as alterações nào preparadas, redefinindo o Git HEAD atual para o estado especificado.
> Se um caminho é passado, funcionará como "não preparado"; se um hash de commit ou uma branch é passado, funcionará como "sem commit".
> Mais informações: <https://git-scm.com/docs/git-reset>.

- Remove tudo da preparação:

`git reset`

- Remove arquivo(s) específico(s) da preparação:

`git reset {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`

- Interativamente remove partes de um arquivo da preparação:

`git reset --patch {{caminho/para/arquivo}}`

- Desfaz o último commit, mantendo suas alterações (e quaisquer outras alteração não confirmadas) no sistema de arquivos:

`git reset HEAD~`

- Desfaz os últimos dois commits, adicionando suas alterações na área de preparação, isso é, preparando-os para o commit:

`git reset --soft HEAD~2`

- Descarta quaisquer alterações sem commit, preparadas ou não (para apenas alterações não preparadas, use o `git checkout`):

`git reset --hard`

- Redefine o repositório para um determinado commit, descartando as alterações com commit, preparadas e sem commit desde então:

`git reset --hard {{commit}}`
