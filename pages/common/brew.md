# brew

> Package manager for macOS and Linux.
> More information: <https://brew.sh>.

- Install the latest stable version of a formula or cask (use `--devel` for development versions):

`brew install {{formula}}`

- Install the latest stable version of a cask (when a GUI and CLI version both exist for a given application):

`brew install --cask {{cask}}`

- List all installed formulae and casks:

`brew list`

- Upgrade an installed formula or cask (if none is given, all installed formulae/casks are upgraded):

`brew upgrade {{formula}}`

- Fetch the newest version of Homebrew and of all formulae and casks from the Homebrew source repository:

`brew update`

- Show formulae and casks that have a more recent version available:

`brew search {{text}}`

- Display information about a formula or a cask (version, installation path, dependencies, etc.):

`brew info {{formula}}`

- Check the local Homebrew installation for potential problems:

`brew doctor`
