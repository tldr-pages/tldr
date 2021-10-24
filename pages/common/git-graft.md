# git graft

> Merge commits from a specific branch into another branch and delete the source branch.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-graft>.

- Merge all commits not present on the target branch from the source branch to target branch, and delete the source branch:

`git graft {{source_branch}} {{target_branch}}`
