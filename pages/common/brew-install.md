# brew install

> Install a Homebrew formula or cask.
> More information: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- Install a formula/cask:

`brew install {{formula|cask}}`

- Build and install a formula from source (dependencies will still be installed from bottles):

`brew install {{[-s|--build-from-source]}} {{formula}}`

- Simulate an installation, downloading the manifest, and printing what would be installed:

`brew install {{[-n|--dry-run]}} {{formula|cask}}`
