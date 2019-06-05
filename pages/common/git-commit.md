# git commit

> Commit files to the repository.
> More information: <https://git-scm.com/docs/git-commit>.

- Commit staged files to the repository with a message:

`git commit -m {{message}}`

- Auto stage all modified files and commit with a message:

`git commit -a -m {{message}}`

- Replace the last commit with currently staged changes:

`git commit --amend`

- Commit only specific (already staged) files:

`git commit {{path/to/my/file1}} {{path/to/my/file2}}`
