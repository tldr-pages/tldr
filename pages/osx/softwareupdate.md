# softwareupdate

> Update macOS from the command line.
> More information: <https://keith.github.io/xcode-man-pages/softwareupdate.8.html>.

- List all available updates:

`softwareupdate -l`

- Install all available updates:

`softwareupdate -i -a`

- Download an update without installing it:

`softwareupdate -d {{update_label}}`

- Install a specific update and automatically restart if required:

`softwareupdate -i {{update_label}} -R`

- List the available full macOS installers:

`softwareupdate --list-full-installers`

- Install Rosetta 2 (for running Intel binaries on Apple Silicon):

`softwareupdate --install-rosetta`
