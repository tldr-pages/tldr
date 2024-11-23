# pacman --sync

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Install a new package:

`sudo pacman -S {{package}}`

- [S]ynchronize and refresh ([y]) the package database along with a sys[u]pgrade (add `--downloadonly` to only download the packages and not update them):

`sudo pacman -Syu`

- Update and [u]pgrade all packages and install a new one without prompting:

`sudo pacman -Syu --noconfirm {{package}}`

- Search ([s]) the package database for a regular expression or keyword:

`pacman -Ss "{{search_pattern}}"`

- Display [i]nformation about a package:

`pacman -Si {{package}}`

- Overwrite conflicting files during a package update:

`sudo pacman -Syu --overwrite {{path/to/file}}`

- [S]ynchronize and [u]pdate all packages, but ignore a specific package (can be used more than once):

`sudo pacman -Syu --ignore {{package1 package2 ...}}`

- Remove not installed packages and unused repositories from the cache (use the flags `Sc` to [c]lean all packages):

`sudo pacman -Sc`
