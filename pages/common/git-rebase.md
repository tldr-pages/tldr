# git rebase

> Reapply commits from one branch on top of another branch.
> Commonly used to "move" an entire branch to another base, creating copies of the commits in the new location.
> More information: <https://git-scm.com/docs/git-rebase>.

- Rebase the current branch on top of another specified branch:

`git rebase {{new_base_branch}}`

- Start an interactive rebase, which allows the commits to be reordered, omitted, combined or modified:

`git rebase -i {{target_base_branch_or_commit_hash}}`

- Continue a rebase that was interrupted by a merge failure, after editing conflicting files:

`git rebase --continue`

- Continue a rebase that was paused due to merge conflicts, by skipping the conflicted commit:

`git rebase --skip`

- Abort a rebase in progress (e.g. if it is interrupted by a merge conflict):

`git rebase --abort`

- Move part of the current branch onto a new base, providing the old base to start from:

`git rebase --onto {{new_base}} {{old_base}}`

- Reapply the last 5 commits in-place, stopping to allow them to be reordered, omitted, combined or modified:

`git rebase -i {{HEAD~5}}`

- Auto-resolve any conflicts by favoring the working branch version (`theirs` keyword has reversed meaning in this case):

`git rebase -X theirs {{branch_name}}`
