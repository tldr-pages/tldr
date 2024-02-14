# kpackagetool5

> KPackage Manager: install, list, remove Plasma packages.
> More information: <https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted#Kpackagetool5>.

- List all known package types that can be installed:

`kpackagetool5 --list-types`

- Install the package from a directory:

`kpackagetool5 --type {{package_type}} --install {{path/to/directory}}`

- Update installed package from a directory:

`kpackagetool5 --type {{package_type}} --upgrade {{path/to/directory}}`

- List installed plasmoids (--global for all users):

`kpackagetool5 --type Plasma/Applet --list --global`

- Remove a plasmoid by name:

`kpackagetool5 --type Plasma/Applet --remove "{{name}}"`
