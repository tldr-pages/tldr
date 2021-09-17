# aura

> The Aura Package Manager: A secure, multilingual package manager for Arch Linux and the AUR.
> More information: <https://github.com/fosskers/aura>.

- Search for packages from the official repositories and AUR:

`aura --aursync --both --search {{package_name|search_regex}}`

- Install a package from the AUR:

`aura --aursync {{package_name}}`

- Update all AUR packages in a verbose mode and remove all make dependencies:

`aura --aursync --diff --sysupgrade --delmakedeps --unsuppress`

- Install a package from the official repositories:

`aura --sync {{package_name}}`

- Synchronize and update all packages from the official repositories:

`aura --sync --refresh --sysupgrade`

- Downgrade a package using the package cache:

`aura --downgrade {{package_name}}`

- Remove a package and its dependencies:

`aura --remove --recursive --unneeded {{package_name}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`aura --orphans --abandon`
