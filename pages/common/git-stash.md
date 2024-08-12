# git stash

> Stash local Git changes in a temporary area.
> More information: <https://git-scm.com/docs/git-stash>.

- Stash current changes with a [m]essage, except new (untracked) files:

`git stash push --message {{optional_stash_message}}`

- Stash current changes, including new ([u]ntracked) files:

`git stash --include-untracked`

- Interactively select [p]arts of changed files for stashing:

`git stash --patch`

- List all stashes (shows stash name, related branch and message):

`git stash list`

- Show the changes as a [p]atch between the stash (default is `stash@{0}`) and the commit back when stash entry was first created:

`git stash show --patch {{stash@{0}}}`

- Apply a stash (default is the latest, named stash@{0}):

`git stash apply {{optional_stash_name_or_commit}}`

- Drop or apply a stash (default is stash@{0}) and remove it from the stash list if applying doesn't cause conflicts:

`git stash pop {{optional_stash_name}}`

- Drop all stashes:

`git stash clear`
