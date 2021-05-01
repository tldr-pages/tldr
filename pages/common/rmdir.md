# rmdir

> Removes a directory.
> More information: <https://www.gnu.org/software/coreutils/rmdir>.

- Remove directory, provided it is empty. Use `rm -r` to remove non-empty directories:

`rmdir {{path/to/directory}}`

- Remove the target and its parent directories (useful for nested dirs):

`rmdir -p {{path/to/directory}}`
