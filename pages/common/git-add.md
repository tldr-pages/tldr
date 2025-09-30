# git add

> Adds changed files to the index.
> More information: <https://git-scm.com/docs/git-add>.

- Add a file to the index:

`git add {{path/to/file}}`

- Add all files (tracked and untracked):

`git add {{[-A|--all]}}`

- Add all files recursively starting from the current folder:

`git add .`

- Only add already tracked files:

`git add {{[-u|--update]}}`

- Also add ignored files:

`git add {{[-f|--force]}}`

- Interactively stage parts of files:

`git add {{[-p|--patch]}}`

- Interactively stage parts of a given file:

`git add {{[-p|--patch]}} {{path/to/file}}`

- Interactively stage a file:

`git add {{[-i|--interactive]}}`
