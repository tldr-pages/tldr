# git cat-file

> Provide content or type and size information for Git repository objects.
> More information: <https://git-scm.com/docs/git-cat-file>.

- Get the [s]ize of the HEAD commit in bytes:

`git cat-file -s HEAD`

- Get the [t]ype (blob, tree, commit, tag) of a given Git object:

`git cat-file -t {{8c442dc3}}`

- Pretty-[p]rint the contents of a given Git object based on its type:

`git cat-file -p {{HEAD~2}}`
