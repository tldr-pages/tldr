# brew

> Package manager for macOS.
> More information: <https://brew.sh>.

- Search for available formulas and casks:

`brew search {{text}}`

- Install the latest stable version of a formula (use `--devel` for development versions):

`brew install {{formula}}`

- List all installed formulae:

`brew list`

- Upgrade an installed formula (if no formula name is given, all installed formulae are upgraded):

`brew upgrade {{formula}}`

- Fetch the newest version of Homebrew and of all formulae from GitHub:

`brew update`

- Remove old versions of installed formulae (if no formula name is given, all installed formulae are processed):

`brew cleanup {{formula}}`

- Display information about a formula (version, installation path, dependencies, etc.):

`brew info {{formula}}`

- Check the local Homebrew installation for potential problems:

`brew doctor`
