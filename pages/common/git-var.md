# git var

> Prints a Git logical variable's value.
> See `git config`, which is preferred over `git var`.
> More information: <https://git-scm.com/docs/git-var>.

- Print the value of a Git logical variable:

`git var {{GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER}}`

- [l]ist all Git logical variables:

`git var -l`
