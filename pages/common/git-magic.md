# git magic

> Abort an ongoing rebase, merge, or cherry-pick.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-magic>.

- Commit changes with a generated message:

`git magic`

- Add untracked files and commit changes with a generated message:

`git magic -a`

- Commit changes with a custom message:

`git magic -m "{{Custom commit message}}"`

- Edit the commit message before committing:

`git magic -em "{{Custom commit message}}"`

- Commit changes and push to remote:

`git magic -p`

- Commit changes with a force push to remote:

`git magic -fp`
