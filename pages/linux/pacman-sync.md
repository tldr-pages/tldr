# pacman sync

> Arch Linux package manager utility.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Install a new package:

`pacman --sync {{package_name}}`

- Synchronize and update all packages (add `--downloadonly` to download only):

`pacman --sync --refresh --sysupgrade`

- Update all packages and install a new one without prompting:

`pacman --sync --refresh --sysupgrade --noconfirm {{package_name}}`

- Search the package database for a regular expression or keyword:

`pacman --sync --search "{{search_pattern}}"`

- Display information about a package:

`pacman --sync --info {{package_name}}`

- Overwrite conflicting files during a package update:

`pacman --sync --refresh --sysupgrade --overwrite {{path/to/file}}`

- Synchronize and update all packages except the ignored (can be used more than once):

`pacman --sync --refresh --sysupgrade --ignore {{package_name}}`

- Remove not installed packages and unused repositories from the cache (use two `--clean` flags to clean all packages):

`pacman --sync --clean`
