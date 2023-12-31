# git stash

> Stash local Git changes in a temporary area.
> More information: <https://git-scm.com/docs/git-stash>.

- Stash current changes, except new (untracked) files:

`git stash push -m {{optional_stash_message}}`

- Stash current changes, including new (untracked) files:

`git stash -u`

- Interactively select parts of changed files for stashing:

`git stash -p`

- List all stashes (shows stash name, related branch and message):

`git stash list`

- Show the changes as a patch between the stash (default is `stash@{0}`) and the commit back when stash entry was first created:

`git stash show -p {{stash@{0}}}`

- Apply a stash (default is the latest, named stash@{0}):

`git stash apply {{optional_stash_name_or_commit}}`

- Drop or apply a stash (default is stash@{0}) and remove it from the stash list if applying doesn't cause conflicts:

`git stash pop {{optional_stash_name}}`

- Drop all stashes:

`git stash clear`
