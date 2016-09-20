# git rebase

> Apply local commits on top of another branch's history.

- Rebase your local branch interactively with the latest changes in local master:

`git rebase -i master`

- Rebase your local branch interactively with the latest changes from upstream:

`git fetch origin; git rebase -i origin/master`

- Handle an active rebase merge failure, after editing conflicting file(s):

`git rebase --continue`

- Abort a rebase in-progress:

`git rebase --abort`

- Rebase your local branch by specifying new base commit and old base commit:

`git rebase --onto {{new_base_commit}} {{old_base_commit}}`
