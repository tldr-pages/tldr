# git add

> Stage changed files for a commit.
> More information: <https://git-scm.com/docs/git-add>.

- Stage a file for a commit:

`git add {{path/to/file}}`

- Add all files (tracked and untracked):

`git add {{[-A|--all]}}`

- Add all files recursively starting from the current folder:

`git add .`

- Only add already tracked files:

`git add {{[-u|--update]}}`

- Add an ignored file:

`git add {{[-f|--force]}} {{path/to/file}}`

- Interactively stage parts of files:

`git add {{[-p|--patch]}}`

- Interactively stage parts of a given file:

`git add {{[-p|--patch]}} {{path/to/file}}`

- Interactively stage a file:

`git add {{[-i|--interactive]}}`
