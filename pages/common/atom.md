# atom

> A cross-platform pluggable text editor.
> Plugins are managed by `apm`.
> More information: <https://atom.io/>.

- Open a file or directory:

`atom {{path/to/file_or_directory}}`

- Open a file or directory in a new window:

`atom -n {{path/to/file_or_directory}}`

- Open a file or directory in an existing window:

`atom --add {{path/to/file_or_directory}}`

- Open atom in safe mode (does not load any additional packages):

`atom --safe`

- Prevent atom from forking into the background, keeping atom attached to the terminal:

`atom --foreground`
