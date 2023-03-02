# Nala

> Package management Utility for Debian and Ubuntu.
> Search for packages using `nala search`.
> More information: 
<https://gitlab.com/volian/nala>.

- Update System:

`nala update`
- Install a package, or update it to the latest available version:

`nala install {{package}}`
- Example: Install the latest version of the package `vim`:

`sudo nala install vim`
- Remove a package:

`sudo nala remove {{package}}`
- Example: Remove the package `vim`:

`nala remove vim` 
- Remove a package and its configuration files:

`nala purge {{package}}`
- Example: Remove the package `vim` and its configuration files:

`nala purge vim`
- Upgrade all installed packages to their newest available versions:

`nala upgrade`
- Clean the local repository by removing package files (`.deb`) from interrupted downloads that can no longer be downloaded:

`nala autoclean`
- Remove all unused packages and dependencies from your Distribution:

`nala autoremove`
- Upgrade installed packages, remove obsolete packages and install additional packages to meet new dependencies:

`nala dist-upgrade`
- Fetch mirrors from the master list for your distribution (Nala will choose the fastest 3 configurable mirrors by testing latency and write them to a file):

`nala fetch`
- Print history of all transactions:

`nala history`