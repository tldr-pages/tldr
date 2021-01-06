# git var

> Prints a Git logical variable.
> More information: <https://git-scm.com/docs/git-var>.

- Print the value of a Git logical variable:

`git var {{GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER}}`

- List all Git logical variables (including those found in `.git/config`; deprecated in favor of `git config -l`):

`git var -l`
