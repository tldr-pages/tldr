# readlink

> Follow symlinks and get symlink information.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/readlink-invocation.html>.

- Get the actual file to which the symlink points:

`readlink {{path/to/file}}`

- Get the absolute path to a file:

`readlink {{[-f|--canonicalize]}} {{path/to/file}}`
