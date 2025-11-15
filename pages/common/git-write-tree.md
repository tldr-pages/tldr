# git write-tree

> Low level utility to create a tree object from the current index.
> More information: <https://git-scm.com/docs/git-write-tree>.

- Create a tree object from the current index:

`git write-tree`

- Create a tree object without checking whether objects referenced by the directory exist in the object database:

`git write-tree --missing-ok`

- Create a tree object that represents a subdirectory (used to write the tree object for a subproject in the named subdirectory):

`git write-tree --prefix {{subdirectory}}/`
