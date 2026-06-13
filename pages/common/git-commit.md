# git commit

> Commit files to the repository.
> More information: <https://git-scm.com/docs/git-commit>.

- Open an editor to write a message and commit staged files to the repository:

`git commit`

- Commit staged files to the repository with the specified message:

`git commit {{[-m|--message]}} "{{message}}"`

- Commit staged files with a message read from a file:

`git commit {{[-F|--file]}} {{path/to/commit_message_file}}`

- Auto stage all modified and deleted files and commit:

`git commit {{[-a|--all]}} {{[-m|--message]}} "{{message}}"`

- Commit staged files and sign them with the specified GPG key (or the one defined in the configuration file if no `key_id` is specified):

`git commit {{[-S|--gpg-sign]}} {{key_id}} {{[-m|--message]}} "{{message}}"`

- Update the last commit by adding the currently staged changes, changing the commit's hash and open an editor to change the message:

`git commit --amend`

- Commit only specific (already staged) files:

`git commit {{path/to/file1 path/to/file2 ...}}`

- Create a commit with the specified message and description:

`git commit {{[-m|--message]}} "{{message}}" {{[-m|--message]}} "{{description}}"`
