# git magic

> Automate add, commit, and push routines.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-magic>.

- Commit changes with a generated message:

`git magic`

- [a]dd untracked files and commit changes with a generated message:

`git magic -a`

- Commit changes with a custom [m]essage:

`git magic -m "{{custom_commit_message}}"`

- [e]dit the commit [m]essage before committing:

`git magic -em "{{custom_commit_message}}"`

- Commit changes and [p]ush to remote:

`git magic -p`

- Commit changes with a [f]orce [p]ush to remote:

`git magic -fp`
