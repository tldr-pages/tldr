# git rebase

> Apply local commits on top of another branch's history.
> This effectively "moves" an entire branch to another base, by creating copies of the commits in the new location.

- Rebase the current branch on top of the master branch:

`git rebase master`

- Start an interactive rebase, which allows the commits to be reordered, omitted, combined or modified:

`git rebase -i {{target_base_branch}}`

- Continue a rebase that was interrupted by a merge failure, after editing conflicting files:

`git rebase --continue`

- Abort a rebase in progress (e.g. if it is interrupted by a merge conflict):

`git rebase --abort`

- Rebase a branch starting from a specific base commit, rather than the common ancestor shared with the target branch:

`git rebase --onto {{new_base_commit}} {{old_base_commit}}`
