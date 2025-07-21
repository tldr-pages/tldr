# pacman --upgrade

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Install one or more packages from files:

`sudo pacman {{[-U|--upgrade]}} {{path/to/package1.pkg.tar.zst path/to/package2.pkg.tar.zst ...}}`

- Install a package without prompting:

`sudo pacman {{[-U|--upgrade]}} --noconfirm {{path/to/package.pkg.tar.zst}}`

- Overwrite conflicting files during a package installation:

`sudo pacman {{[-U|--upgrade]}} --overwrite {{path/to/file}} {{path/to/package.pkg.tar.zst}}`

- Install a package, skipping the dependency version checks:

`sudo pacman {{[-Ud|--upgrade --nodeps]}} {{path/to/package.pkg.tar.zst}}`

- Fetch and print packages that would be affected by upgrade (does not install any packages):

`pacman {{[-Up|--upgrade --print]}} {{path/to/package.pkg.tar.zst}}`

- Display help:

`pacman {{[-Uh|--upgrade --help]}}`
