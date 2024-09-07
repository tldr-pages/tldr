# git mktree

> Build a tree object using `ls-tree` formatted text.
> More information: <https://git-scm.com/docs/git-mktree>.

- Build a tree object and verify that each tree entry’s hash identifies an existing object:

`git mktree`

- Allow missing objects:

`git mktree --missing`

- Read the NUL ([z]ero character) terminated output of the tree object (`ls-tree -z`):

`git mktree -z`

- Allow the creation of multiple tree objects:

`git mktree --batch`

- Sort and build a tree from `stdin` (non-recursive `git ls-tree` output format is required):

`git mktree < {{path/to/tree.txt}}`
