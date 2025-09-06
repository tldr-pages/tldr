# pacman --upgrade

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Install one or more packages from files:

`sudo pacman -U {{path/to/package1.pkg.tar.zst path/to/package2.pkg.tar.zst ...}}`

- Install a package without prompting:

`sudo pacman -U --noconfirm {{path/to/package.pkg.tar.zst}}`

- Overwrite conflicting files during a package installation:

`sudo pacman -U --overwrite {{path/to/file}} {{path/to/package.pkg.tar.zst}}`

- Install a package, skipping the [d]ependency version checks:

`sudo pacman -Ud {{path/to/package.pkg.tar.zst}}`

- Fetch and [p]rint packages that would be affected by upgrade (does not install any packages):

`pacman -Up {{path/to/package.pkg.tar.zst}}`

- Display [h]elp:

`pacman -Uh`
