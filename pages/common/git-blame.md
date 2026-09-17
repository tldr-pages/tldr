# git blame

> Show what commit and author last modified each line of a file.
> More information: <https://git-scm.com/docs/git-blame>.

- Print a file with authorship info (author name and commit hash):

`git blame {{path/to/file}}`

- Print the author's email instead of their name:

`git blame {{[-e|--show-email]}} {{path/to/file}}`

- Print a file with authorship info as of a specific commit:

`git blame {{commit}} {{path/to/file}}`

- Print a file with authorship info before a specific commit:

`git blame {{commit}}~ {{path/to/file}}`

- Print a file with authorship info starting at a given line:

`git blame -L {{123}} {{path/to/file}}`

- Annotate a specific line range of a file:

`git blame -L {{start_line}},{{end_line}} {{path/to/file}}`

- Annotate 10 lines of a file starting at the first line matching a given text:

`git blame -L '/{{text}}/',+10 {{path/to/file}}`

- Annotate a file ignoring whitespaces and line moves:

`git blame -w -C -C -C {{path/to/file}}`
