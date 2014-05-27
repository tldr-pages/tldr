# git stash

> Stash local Git changes in a temporary area

- stash current changes (except new files)

`git stash save {{optional_stash_name}}`

- include new files in the stash (leaves the index completely clean)

`git stash save -u {{optional_stash_name}}`

- list all stashes

`git stash list`

- re-apply the latest stash

`git stash pop`

- re-apply a stash by name

`git stash apply {{stash_name}}`

- drop a stash by an index

`git stash drop stash@{index}`
