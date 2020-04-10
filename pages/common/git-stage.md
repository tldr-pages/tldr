# git stage

> Add file contents to the staging area.
> Synonym of `git add`.
> More information: <https://git-scm.com/docs/git-stage>.

- Add a file to the index:

`git stage {{path/to/file}}`

- Add all files (tracked and untracked):

`git stage -A`

- Only add already tracked files:

`git stage -u`

- Also add ignored files:

`git stage -f`

- Interactively stage parts of files:

`git stage -p`

- Interactively stage parts of a given file:

`git stage -p {{path/to/file}}`

- Interactively stage a file:

`git stage -i`
