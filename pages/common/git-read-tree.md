# git read-tree

> Read tree information into the index.
> See also: `git write-tree`, `git ls-files`.
> More information: <https://git-scm.com/docs/git-read-tree>.

- Replace the index with the contents of a tree (the working tree is not changed):

`git read-tree {{tree}}`

- Reset the index to a tree, discarding unmerged entries, and [u]pdate the working tree to match:

`git read-tree --reset -u {{tree}}`

- Read a tree into the index under a specific subdirectory:

`git read-tree --prefix {{path/to/directory}}/ {{tree}}`

- [m]erge from one tree to another (fast-forward) and [u]pdate the working tree:

`git read-tree -m -u {{tree1}} {{tree2}}`

- Simulate the merge without changing the index or the working tree:

`git read-tree {{[-n|--dry-run]}} -m -u {{tree1}} {{tree2}}`

- Empty the index:

`git read-tree --empty`
