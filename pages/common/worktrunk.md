# worktrunk

> Manage Git worktrees with Worktrunk; commands are run with `wt`.
> More information: <https://worktrunk.dev/>.

- Create and switch to a worktree for a new branch:

`wt switch {{[-c|--create]}} {{branch_name}}`

- Switch to a worktree for an existing branch:

`wt switch {{branch_name}}`

- List worktrees and their status:

`wt list`

- Merge the current worktree into the default branch:

`wt merge`

- Remove a worktree and delete its branch if it is merged:

`wt remove {{branch_name}}`
