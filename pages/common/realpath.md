# realpath

> Display the resolved absolute path for a file or directory.
> More information: <https://www.gnu.org/software/coreutils/realpath>.

- Display the absolute path for a file or directory:

`realpath {{path/to/file_or_directory}}`

- Require all path components to exist:

`realpath --canonicalize-existing {{path/to/file_or_directory}}`

- Resolve ".." components before symlinks:

`realpath --logical {{path/to/file_or_directory}}`

- Disable symlink expansion:

`realpath --no-symlinks {{path/to/file_or_directory}}`

- Suppress error messages:

`realpath --quiet {{path/to/file_or_directory}}`
