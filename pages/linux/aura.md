# aura

> The Aura Package Manager: a secure, multilingual package manager for Arch Linux and the AUR.
> More information: <https://github.com/fosskers/aura>.

- Search for packages from the AUR:

`aura -As {{keyword|regex}}`

- Install a package from the AUR:

`aura -A {{package}}`

- Update all AUR packages in a verbose mode and remove all make dependencies:

`aura -Akua`

- Install a package from the official repositories:

`aura -S {{package}}`

- Synchronize and update all packages from the official repositories:

`aura -Syu`

- Remove a package and its dependencies:

`aura -Rsu {{package}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`aura -Oj`
