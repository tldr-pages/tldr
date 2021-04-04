# git commit

> Commit files to the repository.
> More information: <https://git-scm.com/docs/git-commit>.

- Commit staged files to the repository with a message:

`git commit -m "{{message}}"`

- Commit staged files with a message read from a file:

`git commit --file {{path/to/commit_message_file}}`

- Auto stage all modified files and commit with a message:

`git commit -a -m "{{message}}"`

- Update the last commit by adding the currently staged changes, changing the commit's hash:

`git commit --amend`

- Commit only specific (already staged) files:

`git commit {{path/to/file1}} {{path/to/file2}}`
