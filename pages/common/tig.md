# tig

> A text-mode interface for Git.
> More information: <https://github.com/jonas/tig>.

- Show the sequence of commits starting from the current one in reverse chronological order:

`tig`

- Show the history of a specific branch:

`tig {{branch}}`

- Show the history of specific files or directories:

`tig {{path1 path2 ...}}`

- Show the difference between two references (such as branches or tags):

`tig {{base_ref}}..{{compared_ref}}`

- Display commits from all branches and stashes:

`tig --all`

- Start in stash view, displaying all saved stashes:

`tig stash`
