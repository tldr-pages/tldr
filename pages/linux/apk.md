# apk

> Alpine Linux package management tool.
> More information: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Update repository indexes from all remote repositories:

`apk update`

- Install a new package:

`apk add {{package}}`

- Remove a package:

`apk del {{package}}`

- Repair a package or upgrade it without modifying main dependencies:

`apk fix {{package}}`

- Search for a package via keywords:

`apk search {{keywords}}`

- Display information about a specific package:

`apk info {{package}}`
