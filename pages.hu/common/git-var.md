# git var

> Egy Git logikai változó értékének kiírása. Lásd: `git config`, amely előnyben részesül a `git var` helyett. További információ: <https://git-scm.com/docs/git-var>.

- Egy Git logikai változó értékének kiírása:

`git var {{GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER}}`

- \[l\]ist minden Git logikai változó értéke:

`git var -l`
