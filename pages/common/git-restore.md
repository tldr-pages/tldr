# git restore

> Restore working tree files. Requires git version 2.23+.
> See also `git checkout`.
> More information: <https://git-scm.com/docs/git-restore/>.

- Restore a file that was accidentally deleted:

`git restore {{path/to/file}}`

- Restore a file to an earlier version:

`git restore --source {{commit}} {{path/to/file}}`

- Restore all the files in the current working tree to the last committed version:

`git restore .`
