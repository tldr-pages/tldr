# wt switch

> Switch to a Worktrunk worktree, creating it if needed.
> More information: <https://worktrunk.dev/switch/>.

- Switch to a worktree for a branch, creating the worktree if needed:

`wt switch {{branch_name}}`

- Create a new branch and worktree, then switch to it:

`wt switch {{[-c|--create]}} {{branch_name}}`

- Create a branch from a specific base branch:

`wt switch --create {{branch_name}} --base {{base_branch}}`

- Return to the previous worktree:

`wt switch -`

- Switch to the branch for a GitHub pull request:

`wt switch pr:{{pr_number}}`
