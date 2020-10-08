# legit

> Complementary command-line interface for Git.
> More information: <https://frostming.github.io/legit>.

- Switch to a specified branch, stashing and restoring unstaged changes:

`git switch <branch>`

- Synchronize current branch. Auto-merge/rebase, un/stash:

`git sync`

- Publish branch to remote server:

`git publish {{branch}}`

- Remove branch from remote server:

`git unpublish {{branch}}`

- List of branches + publication status:

`git branches {{wildcard pattern}}`

- Remove the last commit from history:

`git undo {{--hard}}`
