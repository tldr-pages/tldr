# tre

> Show the contents of the current directory as a tree.
> Respects the `.gitignore` settings by default.
> More information: <https://github.com/dduan/tre#everything-else>.

- Print directories only:

`tre {{[-d|--directories]}}`

- Print JSON containing files in the tree hierarchy instead of the normal tree diagram:

`tre {{[-j|--json]}}`

- Print files and directories up to the specified depth limit (where 1 means the current directory):

`tre {{[-l|--limit]}} {{depth}}`

- Print all hidden files and directories using the specified colorization mode:

`tre {{[-a|--all]}} {{[-c|--color]}} {{automatic|always|never}}`

- Print files within the tree hierarchy, assigning a shell alias to each file that, when called, will open the associated file using the provided `command` (or in `$EDITOR` by default):

`tre {{[-e|--editor]}} {{command}}`

- Print files within the tree hierarchy, excluding all paths that match the provided `regex`:

`tre {{[-E|--exclude]}} {{regex}}`

- Display version:

`tre {{[-V|--version]}}`

- Display help:

`tre {{[-h|--help]}}`
