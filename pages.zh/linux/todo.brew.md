# brew

> The Homebrew package manager for Linux.

- Search for available formulas:

`brew search {{text}}`

- Install the latest stable version of a formula (use `--devel` for development versions):

`brew install {{formula}}`

- List all installed formulae:

`brew list`

- Upgrade an installed formula (if no formula name is given, all installed formulae are upgraded):

`brew upgrade {{formula}}`

- Fetch the newest version of Linuxbrew and of all formulae from GitHub:

`brew update`

- Show formulae that have a more recent version available:

`brew outdated`

- Display information about a formula (version, installation path, dependencies, etc.):

`brew info {{formula}}`

- Check the local Linuxbrew installation for potential problems:

`brew doctor`
