# realpath

> Display the resolved absolute path for a file or directory.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>.

- Display the absolute path for a file or directory:

`realpath {{path/to/file_or_directory}}`

- Require all path components to exist:

`realpath {{[-e|--canonicalize-existing]}} {{path/to/file_or_directory}}`

- Resolve `..` components before symlinks:

`realpath {{[-L|--logical]}} {{path/to/file_or_directory}}`

- Disable symlink expansion:

`realpath {{[-s|--no-symlinks]}} {{path/to/file_or_directory}}`

- Suppress error messages:

`realpath {{[-q|--quiet]}} {{path/to/file_or_directory}}`
