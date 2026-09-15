# try-rs

> Manage temporary project workspaces with an interactive TUI.
> More information: <https://try-rs.org/#usage>.

- Open the interactive TUI:

`try-rs`

- Create or jump to a named experiment:

`try-rs {{experiment_name}}`

- Clone a repository into a dated folder:

`try-rs {{https://github.com/user/repository}}`

- Clone a repository into a specific destination folder:

`try-rs {{https://github.com/user/repository}} {{destination_name}}`

- Create a Git worktree from the current repository:

`try-rs --worktree {{worktree_name}}`

- Generate shell integration for the specified shell:

`try-rs --setup {{bash|fish|zsh|nu-shell|power-shell}}`
