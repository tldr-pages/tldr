# git blame

> Show commit hash and last author on each line of a file.
> More information: <https://git-scm.com/docs/git-blame>.

- Print file with author name and commit hash on each line:

`git blame {{path/to/file}}`

- Print file with author email and commit hash on each line:

`git blame {{[-e|--show-email]}} {{path/to/file}}`

- Print file with author name and commit hash on each line at a specific commit:

`git blame {{commit}} {{path/to/file}}`

- Print file with author name and commit hash on each line before a specific commit:

`git blame {{commit}}~ {{path/to/file}}`

- Jump to the parent of a specific commit and track a specific text and 10 of its following lines:

`git blame -L '/{{text}}/',+10 {{a82812aa}}^ {{path/to/file}}`

- Print author name and commit hash information for a specific line range:

`git blame -L {{start_line}},{{end_line}} {{path/to/file}}`

- Ignore whitespaces and line moves:

`git blame -w -C -C -C {{path/to/file}}`
