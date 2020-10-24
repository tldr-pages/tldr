# git restore

> Restore working tree files. Requires git version 2.23+.
> See also `git checkout`.
> More information: <https://git-scm.com/docs/git-restore/>.

- Restore a deleted file from the contents of the current commit (HEAD):

`git restore {{path/to/file}}`

- Restore a file to a version from a different commit:

`git restore --source {{commit}} {{path/to/file}}`

- Undo any uncommitted changes to tracked files, reverting to the current HEAD:

`git restore .`
