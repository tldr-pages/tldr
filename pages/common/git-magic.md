# git magic

> Automate add, commit, and push routines.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-magic>.

- Commit changes with a generated message:

`git magic`

- [a]dd untracked files and commit changes with a generated message:

`git magic -a`

- Commit changes with a custom message:

`git magic -m "{{custom_commit_message}}"`

- Edit the commit message before committing:

`git magic -em "{{custom_commit_message}}"`

- Commit changes and push to remote:

`git magic -p`

- Commit changes with a force push to remote:

`git magic -fp`
