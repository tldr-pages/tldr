# dot_clean

> Merge ._* files with corresponding native files.
> More information: <https://keith.github.io/xcode-man-pages/dot_clean.1.html>.

- Merge all `._*` files recursively:

`dot_clean {{path/to/directory}}`

- Don't recursively merge all `._*` in a directory (flat merge):

`dot_clean -f {{path/to/directory}}`

- Merge and delete all `._*` files:

`dot_clean -m {{path/to/directory}}`

- Only delete `._*` files if there's a matching native file:

`dot_clean -n {{path/to/directory}}`

- Follow symlinks:

`dot_clean -s {{path/to/directory}}`

- Print verbose output:

`dot_clean -v {{path/to/directory}}`
