# git sync

> Sync local branches with remote branches.
> Part of `git-extras`.
> More information: <https://manned.org/git-sync>.

- Sync the current local branch with its remote branch:

`git sync`

- Sync the current local branch with the remote main branch:

`git sync origin main`

- Sync without cleaning untracked files:

`git sync {{[-s|--soft]}} {{remote_name}} {{branch_name}}`
