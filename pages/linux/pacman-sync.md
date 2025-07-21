# pacman --sync

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Install a new package:

`sudo pacman {{[-S|--sync]}} {{package}}`

- Synchronize and refresh the package database along with a sysupgrade (add `--downloadonly` to only download the packages and not update them):

`sudo pacman {{[-Syu|--sync --refresh --sysupgrade]}}`

- Update and upgrade all packages and install a new one without prompting:

`sudo pacman {{[-Syu|--sync --refresh --sysupgrade]}} --noconfirm {{package}}`

- Search the package database for a regular expression or keyword:

`pacman {{[-Ss|--sync --search]}} "{{search_pattern}}"`

- Display information about a package:

`pacman {{[-Si|--sync --info]}} {{package}}`

- Overwrite conflicting files during a package update:

`sudo pacman {{[-Syu|--sync --refresh --sysupgrade]}} --overwrite {{path/to/file}}`

- Remove not installed packages and unused repositories from the cache (use the flags `Sc` to clean all packages):

`sudo pacman {{[-Sc|--sync --clean]}}`

- Specify the package version that should be installed:

`sudo pacman {{[-S|--sync]}} {{package}}={{version}}`
