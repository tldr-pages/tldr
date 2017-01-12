# brew

> The Homebrew package manager for Linux.

- Search formula:

`brew search {{text}}`

- Install formula:

`brew install {{formula}}`

- List installed files for formulae or list all installed formulae if no formula specified, argument --verbose is to recursively list files of all subdirectories.:

`brew list --verbose {{formula}}`

- Get latest version of installed formula (passing no formula updates all installed formulae):

`brew upgrade {{formula}}`

- Update brew:

`brew update`

- Switch version of formula:

`brew switch {{formula}} {{version}}`

- Display information about formula, which contains formula version, installed path, dependencies, etc.:

`brew info {{formula}}`
