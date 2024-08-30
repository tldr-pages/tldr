# git add

> Adds changed files to the index.
> More information: <https://git-scm.com/docs/git-add>.

- Add a file to the index:

`git add {{path/to/file}}`

- Add all files (tracked and untracked):

`git add {{--all|-A}}`

- Add all files in the current folder:

`git add .`

- Only add already tracked files:

`git add {{--update|-u}}`

- Also add ignored files:

`git add {{--force|-f}}`

- Interactively stage parts of files:

`git add {{--patch|-p}}`

- Interactively stage parts of a given file:

`git add {{--patch|-p}} {{path/to/file}}`

- Interactively stage a file:

`git add {{--interactive|-i}}`
