# apk

> Alpine Linux package management tool.

- Update repository indexes from all remote repositories:

`apk update`

- Install a new package:

`apk add {{package}}`

- Remove a package:

`apk del {{package}}`

- Repair package or upgrade it without modifying main dependencies:

`apk fix {{package}}`

- Search package via keyword:

`apk search {{keyword}}`

- List the packages installed in the System:

`apk info {{package}}`
