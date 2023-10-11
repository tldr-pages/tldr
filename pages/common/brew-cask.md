# brew --cask

> CLI workflow for the administration of macOS applications distributed as binaries.
> This command was previously called `brew cask`, it has been deprecated in favor of the `brew --cask` flag.
> More information: <https://github.com/Homebrew/homebrew-cask>.

- Search for formulas and casks:

`brew search {{text}}`

- Install a cask:

`brew install --cask {{cask_name}}`

- List all installed casks:

`brew list --cask`

- List installed casks that have newer versions available:

`brew outdated --cask`

- Upgrade an installed cask (if no cask name is given, all installed casks are upgraded):

`brew upgrade --cask {{cask_name}}`

- Uninstall a cask:

`brew uninstall --cask {{cask_name}}`

- Uninstall a cask and remove related settings and files:

`brew zap --cask {{cask_name}}`

- Display information about a given cask:

`brew info --cask {{cask_name}}`
