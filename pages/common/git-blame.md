# git blame

> Show commit hash and last author on each line of a file.
> More information: <https://git-scm.com/docs/git-blame>.

- Print file with author name and commit hash on each line:

`git blame {{file}}`

- Print file with author email and commit hash on each line:

`git blame -e {{file}}`

- Print file with author name and commit hash on each line at a specific commit:

`git blame {{commit}} {{path/to/file}}`

- Print file with author name and commit hash on each line before a specific commit:

`git blame {{commit}}~ {{path/to/file}}`
