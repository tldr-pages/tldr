# aura

> The Aura Package Manager: A secure, multilingual package manager for Arch Linux and the AUR.
> More information: <https://github.com/fosskers/aura>.

- Search for packages from the repos and AUR:

`aura -As --both {{package_name|search_regex}}`

- Update all AUR packages in a verbose mode and remove all make dependencies:

`aura -Akuax`

- Install a package from the AUR:

`aura -A {{package_name}}`

- Install a package from the system repos:

`aura -S {{package_name}}`

- Update all system repo packages:

`aura -Syu`

- Downgrade a package from the package cache:

`aura -C {{package_name}}`

- Remove both an installed package and its dependencies:

`aura -Rs {{package_name}}`

- Uninstall all orphan packages:

`aura -Oj`
