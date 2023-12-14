# git mktree

> Build a tree-object using ls-tree formatted text.
> More information: <https://git-scm.com/docs/git-mktree>.

- Allow for missing objects which bypass the default behavior that verifies each tree entry has an existing object:

`git mktree --missing`

- Read the NUL-terminated output of the tree-object:

`git mktree -z`

- Allow for the creation of multiple tree object:

`git mktree --batch`
