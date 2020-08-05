# git stash

> Stash local Git changes in a temporary area.
> More information: <https://git-scm.com/docs/git-stash>.

- Stash current changes, except new (untracked) files:

`git stash [push -m {{optional_stash_message}}]`

- Stash current changes, including new (untracked) files:

`git stash -u`

- Interactively select parts of changed files for stashing:

`git stash -p`

- List all stashes (shows stash name, related branch and message):

`git stash list`

- Display changes in a stash (default is the latest, named stash@{0}):

`git stash show -p {{optional_stash_name_or_commit}}`

- Apply a stash (default is stash@{0}), use `stash pop` to apply the stash and remove it from the stash list:

`git stash apply {{optional_stash_name_or_commit}}`

- Drop a stash (default is stash@{0}):

`git stash drop {{optional_stash_name}}`

- Drop all stashes:

`git stash clear`
