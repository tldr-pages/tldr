# git sync

> Sync local branches with remote branches.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sync>.

- Sync the current local branch with its remote branch:

`git sync`

- Sync the current local branch with the remote main branch:

`git sync origin main`

- Sync without cleaning untracked files:

`git sync -s {{remote_name}} {{branch_name}}`
