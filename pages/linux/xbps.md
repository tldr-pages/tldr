# xbps

> The X Binary Package System (or xbps) is the binary package system used by Void Linux.

- Install packages:
`xbps-install -S package_name1 package_name2`

- Search a package:
`xbps-query -Rs package_name`

- Remove a package, leaving all of its dependencies installed:
`xbps-remove package_name`

- Remove a package and all of its dependencies that are not required by other packages:
`xbps-remove -R package_name`

- Synchronize your repository databases and update your system and dependencies:
`xbps-install -Su`
