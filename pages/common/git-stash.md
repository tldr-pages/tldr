# git stash

> Stash local Git changes in a temporary area.
> More information: <https://git-scm.com/docs/git-stash>.

- Stash the current uncommitted changes:

`git stash`

- Stash current changes, including new untracked files:

`git stash {{[-u|--include-untracked]}}`

- Interactively select parts of changed files for stashing:

`git stash {{[-p|--patch]}}`

- List all stashes:

`git stash list`

- Show the changes as a patch between the stash and the commit back when stash entry was first created:

`git stash show {{[-p|--patch]}}}`

- Apply a stash and remove it from the stash list if applying doesn't cause conflicts:

`git stash pop`

- Delete the latest stash:

`git stash drop`

- Delete all stashes:

`git stash clear`
