# git feature

> Create or merge feature branches.
> Feature branches obey the format feature/<name>.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-feature>.

- Create and switch to a new feature branch:

`git feature {{feature_branch}}`

- Merge a feature branch into the current branch creating a merge commit:

`git feature finish {{feature_branch}}`

- Merge a feature branch into the current branch squashing the changes into one commit:

`git feature finish --squash {{feature_branch}}`

- Send changes from a specific feature branch to its remote counterpart:

`git feature {{feature_branch}} --remote {{remote_name}}`
