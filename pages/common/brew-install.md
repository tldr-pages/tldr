# brew install

> Install a Homebrew formula or cask.
> More information: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- Install a formula/cask:

`brew install {{formula|cask}}`

- Build and install a formula from source (dependencies will still be installed from bottles):

`brew install --build-from-source {{formula}}`

- Download the manifest, print what would be installed but don't actually install anything:

`brew install --dry-run {{formula|cask}}`
