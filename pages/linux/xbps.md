# xbps

> The X Binary Package System (or xbps) is the binary package system used by Void Linux.

- Install packages; Option -S --synchronize:

`xbps-install --synchronize {{package_name1}} {{package_name2}}`

- Search for a package; Option -R --repository; Mode -s --search; Shorthand -Rs:

`xbps-query --repository -s {{package_name}}`

- Remove a package, leaving all of its dependencies installed:

`xbps-remove {{package_name}}`

- Remove a package and all of its dependencies that are not required by other packages; Option -R --recursive:

`xbps-remove --recursive {{package_name}}`

- Synchronize your repository databases and update your system and dependencies; Options -S --synchronize, -u --update:

`xbps-install --synchronize -u`
