# git stash

> Stash local Git changes in a temporary area.

- Stash current changes, except new (untracked) files:

`git stash [save {{optional_stash_message}}]`

- Stash current changes, including new (untracked) files:

`git stash -u`

- Interactively select parts of changed files for stashing:

`git stash -p`

- List all stashes (shows stash name, related branch and message):

`git stash list`

- Apply a stash (default is the latest, named stash@{0}):

`git stash apply {{optional_stash_name_or_commit}}`

- Apply a stash (default is stash@{0}), and remove it from the stash list if applying doesn't cause conflicts:

`git stash pop {{optional_stash_name}}`

- Drop a stash (default is stash@{0}):

`git stash drop {{optional_stash_name}}`

- Drop all stashes:

`git stash clear`
