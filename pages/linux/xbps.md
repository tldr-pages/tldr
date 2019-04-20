# xbps

> The X Binary Package System (or xbps) is the binary package system used by Void Linux.

- Install packages and synchronize them with the remote repository:

`xbps-install --synchronize {{package_name1}} {{package_name2}}`

- Search for a package in the remote repository:

`xbps-query --repository -s {{package_name}}`

- Remove a package, leaving all of its dependencies installed:

`xbps-remove {{package_name}}`

- Remove a package and all of its dependencies recursively that are not required by other packages:

`xbps-remove --recursive {{package_name}}`

- Synchronize your repository databases and update your system and dependencies:

`xbps-install --synchronize -u`
