# git create-branch

> Git-ág létrehozása egy adattárban. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-create-branch>.

- Helyi ág létrehozása:

`git create-branch {{branch_name}}`

- Létrehoz egy ágat helyileg és az origón:

`git create-branch --remote {{branch_name}}`

- Létrehoz egy ágat helyben és az upstream-en (forkokon keresztül):

`git create-branch --remote upstream {{branch_name}}`
