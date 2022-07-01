# deb-get

> `apt-get` functionality for `.deb` packages published in third party repositories or via direct download.
> It works on Debian, Ubuntu, and derivative distributions.
> More information: <https://github.com/wimpysworld/deb-get>.

- Update the list of available packages and versions (it's recommended to run this before other commands):

`sudo deb-get update`

- Search for a given package:

`sudo deb-get search {{package}}`

- Show information for a package:

`sudo deb-get show {{package}}`

- Install a package, or update it to the latest available version:

`sudo deb-get install {{package}}`

- Remove a package (using `purge` instead also removes its configuration files):

`sudo deb-get remove {{package}}`

- Upgrade all installed packages to their newest available versions:

`sudo deb-get upgrade`

- List all packages:

`deb-get list`
