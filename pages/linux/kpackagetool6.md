# kpackagetool6

> KPackage Manager: install, list, remove Plasma packages.
> More information: <https://manned.org/kpackagetool6>.

- List all known package types that can be installed:

`kpackagetool6 --list-types`

- Install the package from a directory:

`kpackagetool6 --type {{package_type}} --install {{path/to/directory}}`

- Update installed package from a directory:

`kpackagetool6 --type {{package_type}} --upgrade {{path/to/directory}}`

- List installed plasmoids (`--global` for all users):

`kpackagetool6 --type Plasma/Applet --list --global`

- Remove a plasmoid by name:

`kpackagetool6 --type Plasma/Applet --remove "{{name}}"`
