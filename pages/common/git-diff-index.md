# git diff-index

> Compare the working directory with a specific commit or tree object.
> More information: <https://git-scm.com/docs/git-diff-index>.

- Compare the working directory with a specific commit:

`git diff-index {{commit}}`

- Compare a specific file or directory in working directory with a commit:

`git diff-index {{commit}} {{path/to/file_or_directory}}`

- Compare the working directory with the index (staging area) to check for staged changes:

`git diff-index --cached {{commit}}`

- Suppress output and return an exit status to check for differences:

`git diff-index --quiet {{commit}}`
