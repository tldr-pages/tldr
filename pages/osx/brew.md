# brew

> Package manager for macOS.
> More information: <https://brew.sh>.

- Search for available formulae and casks:

`brew search {{text}}`

- Install the latest stable version of a formula (use `--devel` for development versions):

`brew install {{formula}}`

- List all installed formulae:

`brew list`

- List installed formulae that are not dependencies of another installed formula:

`brew leaves`

- Upgrade an installed formula (if no formula name is given, all installed formulae are upgraded):

`brew upgrade {{formula}}`

- Fetch the newest version of Homebrew and of all formulae from GitHub:

`brew update`

- Display information about a formula (version, installation path, dependencies, etc.):

`brew info {{formula}}`

- Check the local Homebrew installation for potential problems:

`brew doctor`
