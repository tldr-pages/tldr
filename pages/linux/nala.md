
# nala

> Package management utility for Debian and Ubuntu.
> Search for packages using `nala search`.
> More information: <https://gitlab.com/volian/nala>.

- Update System:

`nala update`

- Install a package, or update it to the latest available version:

`nala install {{package}}`

- Remove a package:

`nala remove {{package}}`

- Remove a package and its configuration files:

`nala purge {{package}}`

- Upgrade all installed packages to their newest available versions:

`nala upgrade`

- Clean the local repository - removing package files (`.deb`) from interrupted downloads that can no longer be downloaded:

`nala autoclean`

- Remove all packages that are no longer needed:

`nala autoremove`

- Upgrade installed packages (like `upgrade`), but remove obsolete packages and install additional packages to meet new dependencies:

`nala dist-upgrade`

- Nala will then go get all the mirrors from the respective master list. Once done we test the latency and score each mirror. Nala will choose the fastest 3 mirrors (configurable) and write them to a file.

`nala fetch`

- History

`nala history`



