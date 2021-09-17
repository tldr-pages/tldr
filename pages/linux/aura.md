# aura

> The Aura Package Manager: A secure, multilingual package manager for Arch Linux and the AUR.
> More information: <https://github.com/fosskers/aura>.

- Search for packages from the official repositories and AUR:

`aura -As --both {{package_name|search_regex}}`

- Update all AUR packages in a verbose mode and remove all make dependencies:

`aura -Akuax`

- Install a package from the AUR:

`aura -A {{package_name}}`

- Install a package from the official repositories:

`aura -S {{package_name}}`

- Synchronize and update all packages from the official repositories:

`aura -Syu`

- Downgrade a package using the package cache:

`aura -C {{package_name}}`

- Remove a package and its dependencies:

`aura -Rs {{package_name}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`aura -Oj`
