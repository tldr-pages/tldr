# tre

> Show the contents of the current directory as a tree.
> Respects `.gitignore` settings, by default.
> More information: <https://github.com/dduan/tre>.

- Print directories only:

`tre -d`

- Print JSON containing files in the tree hierarchy, instead of the normal tree diagram:

`tre -j`

- Print files and directories up to the specified depth limit (where 1 means the current directory):

`tre -l {{depth}}`

- Print all hidden files and directories using the specified colorization mode (eg. `automatic`, `always`, `never`):

`tre -a -c {{when}}`

- Print files within the tree hierarchy, assigning a shell alias to each file that, when called, will open the associated file using the provided `command`:

`tre -e {{command}}`

- Print files within the tree hierarchy, excluding all paths that do not match the provided RegExp pattern:

`tre -E {{pattern}}`

- Display version:

`tre --version`

- Display help:

`tre --help`