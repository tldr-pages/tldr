# git stash

> Stash local Git changes in a temporary area.

- Stash current changes (except new files):

`git stash save {{optional_stash_message}}`

- Include new files in the stash (leaves the index completely clean):

`git stash save -u {{optional_stash_message}}`

- List all stashes:

`git stash list`

- Apply a stash (default is the latest, named stash@{0}):

`git stash apply {{optional_stash_name_or_commit}}`

- Apply a stash (default is stash@{0}), and remove it from the list if applying doesn't cause conflicts:

`git stash pop {{optional_stash_name}}`

- Drop a stash (default is stash@{0}):

`git stash drop {{optional_stash_name}}`
