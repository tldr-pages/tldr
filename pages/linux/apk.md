# apk

> Alpine Linux package management tool.
> More information: <https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper>.

- Update repository indexes and upgrade all packages:

`apk upgrade {{[-U|--update-cache]}}`

- Only update repository indexes:

`apk update`

- Install a new package:

`apk add {{package}}`

- Remove a package:

`apk del {{package}}`

- Repair/Reinstall a package without modifying main dependencies:

`apk fix {{package}}`

- Search for packages with a keyword in their name and list results with descriptions:

`apk search {{[-v|--verbose]}} {{keyword}}`

- Search for packages with a keyword in their description:

`apk search {{[-d|--description]}} {{keyword}}`

- Display information about a specific package:

`apk info {{package}}`
