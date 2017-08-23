# brew

> The Homebrew package manager for Linux.

- Search for available formulas:

`brew search {{text}}`

- Install the latest stable version of a formula (use `--devel` for development versions):

`brew install {{formula}}`

- List all installed formulae:

`brew list`

- Update an installed formula (passing no `{{formula}}` updates all installed formulae):

`brew upgrade {{formula}}`

- Fetch the newest version of Linuxbrew and all formulae from GitHub:

`brew update`

- Show formulae that have an updated version available:

`brew outdated`

- Display information about a formula (version, installation path, dependencies, etc.):

`brew info {{formula}}`

- Check your Linuxbrew installation for potential problems:

`brew doctor`
