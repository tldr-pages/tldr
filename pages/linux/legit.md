# legit

> Complementary command-line interface for Git.
> More information: <https://frostming.github.io/legit>.

- Switch to a specified branch, stashing and restoring unstaged changes:

`git switch {{target_branch}}`

- Synchronize current branch, automatically merging or rebasing, and stashing and unstashing:

`git sync`

- Publish a specified branch to the remote server:

`git publish {{branch_name}}`

- Remove a branch from the remote server:

`git unpublish {{branch_name}}`

- List all branches and their publication status:

`git branches {{glob_pattern}}`

- Remove the last commit from the history:

`git undo {{--hard}}`
