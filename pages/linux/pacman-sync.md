# pacman --sync

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Install a new package:

`sudo pacman --sync {{package}}`

- [S]ynchronize and update all packages (add `--downloadonly` to download the packages and not update them):

`sudo pacman --sync --refresh --sysupgrade`

- [U]pdate all packages and install a new one without prompting:

`sudo pacman --sync --refresh --sysupgrade --noconfirm {{package}}`

- Search ([Ss]) the package database for a regular expression or keyword:

`pacman --sync --search "{{search_pattern}}"`

- Display [i]nformation about a package:

`pacman --sync --info {{package}}`

- Overwrite conflicting files during a package update:

`sudo pacman --sync --refresh --sysupgrade --overwrite {{path/to/file}}`

- [S]ynchronize and update all packages, but ignore a specific package (can be used more than once):

`sudo pacman --sync --refresh --sysupgrade --ignore {{package}}`

- Remove not installed packages and unused repositories from the cache (use two `--clean` flags to clean all packages):

`sudo pacman --sync --clean`
