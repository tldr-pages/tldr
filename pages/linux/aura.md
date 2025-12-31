# aura

> The Aura Package Manager: a secure, multilingual package manager for Arch Linux and the AUR.
> More information: <https://github.com/fosskers/aura>.

- Search for packages from the AUR:

`aura {{[-As|--aursync --search]}} {{keyword|regex}}`

- Install a package from the AUR:

`aura {{[-A|--aursync]}} {{package}}`

- Update all AUR packages in a verbose mode and remove all make dependencies:

`aura {{[-Akua|--aursync --diff --sysupgrade --delmakedeps]}}`

- Install a package from the official repositories:

`aura {{[-S|--sync]}} {{package}}`

- Synchronize and update all packages from the official repositories:

`aura {{[-Syu|--sync --refresh --sysupgrade]}}`

- Remove a package and its dependencies:

`aura {{[-Rsu|--remove --recursive --unneeded]}} {{package}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`aura {{[-Oj|--orphans --abandon]}}`
