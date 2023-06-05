# git commit

> Commit files to the repository.
> More information: <https://git-scm.com/docs/git-commit>.

- Commit staged files to the repository with a message:

`git commit --message "{{message}}"`

- Commit staged files with a message read from a file:

`git commit --file {{path/to/commit_message_file}}`

- Auto stage all modified and deleted files and commit with a message:

`git commit --all --message "{{message}}"`

- Commit staged files and sign them with the specified GPG key (or the one defined in the config file if no argument is specified):

`git commit --gpg-sign {{key_id}} --message "{{message}}"`

- Update the last commit by adding the currently staged changes, changing the commit's hash:

`git commit --amend`

- Commit only specific (already staged) files:

`git commit {{path/to/file1}} {{path/to/file2}}`

- Create a commit, even if there are no staged files:

`git commit --message "{{message}}" --allow-empty`
