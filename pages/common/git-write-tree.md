# git write-tree

> Low level utility to create a tree object from the current index.

- Create a tree object without checking whether objects referenced by the directory exist in the object database:

`git write-tree --missing-ok`

- Create a tree object that represents a subdirectory {{prefix}}. This can be used to write the tree object for a subproject that is in the named subdirectory:

`git write-tree --prefix={{prefix/}}`
