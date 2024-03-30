# git annotate

> Show commit hash and last author on each line of a file.
> See `git blame`, which is preferred over `git annotate`.
> `git annotate` is provided for those familiar with other version control systems.
> More information: <https://git-scm.com/docs/git-annotate>.

- Print a file with the author name and commit hash prepended to each line:

`git annotate {{path/to/file}}`

- Print a file with the author [e]mail and commit hash prepended to each line:

`git annotate -e {{path/to/file}}`

- Print only rows that match a regular expression:

`git annotate -L :{{regexp}} {{path/to/file}}`
