# brew

> Package manager for OS X.

- Search formula:

`brew search {{text}}`

- Install formula:

`brew install {{formula}}`

- List installed files for formulae, argument --verbose is to recursively list files of all subdirectories, it's optional:

`brew list --verbose {{formula}}`

- Get latest version of installed formula (passing no formula updates all installed formulae):

`brew upgrade {{formula}}`

- Update brew:

`brew update`

- Switch version of formula:

`brew switch {{formula}} {{version}}`

- Display information about formula, which contains formula version, installed path, dependencies, etc.

`brew info {{formula}}`
