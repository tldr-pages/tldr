# kpackagetool5

> KPackage Manager: Install, list, remove Plasma packages.
> More information: <https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted#Kpackagetool5>.

- List all known package types that can be installed:

`kpackagetool5 --list-types`

- Install the package from a directory:

`kpackagetool5 -t {{package_type}} -i {{path/to/directory}}`

- Update installed package from a directory:

`kpackagetool5 -t {{package_type}} -u {{path/to/directory}}`

- List installed plasmoids (-g, or --global for all users):

`kpackagetool5 -t Plasma/Applet -l -g`

- Remove a plasmoid by name:

`kpackagetool5 -t Plasma/Applet -r "{{name}}"`
