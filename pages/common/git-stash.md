# git stash

> Stash local Git changes in a temporary area.

- Stash current changes (except new files):

`git stash save {{optional_stash_name}}`

- Include new files in the stash (leaves the index completely clean):

`git stash save -u {{optional_stash_name}}`

- List all stashes:

`git stash list`

- Re-apply the latest stash:

`git stash pop`

- Re-apply a stash by name:

`git stash apply {{stash_name}}`

- Drop a stash by an index:

`git stash drop stash@{index}`
