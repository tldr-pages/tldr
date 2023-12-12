# git mktree

> Build a tree-object using ls-tree formatted text.
> More information: <https://git-scm.com/docs/git-mktree>.

- Allows for missing objects bypassing the default behavior which usually verifies each tree entry has an existing object:

`git mktree --missing`

- Reads the NUL-terminated output of the tree-object:

`git mktree -z`

- Allows for the creation of multiple tree object:

`git mktree -- batch`