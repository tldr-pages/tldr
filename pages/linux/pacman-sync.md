# pacman --sync

> Synchronize packages from remote repositories.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Install a new package:

`sudo pacman -S {{package}}`

- [S]ynchronize and refresh ([y]) the package database along with a sys[u]pgrade (add `--downloadonly` to only download the packages and not update them):

`sudo pacman -Syu`

- Update and [u]pgrade all packages and install a new one without prompting:

`sudo pacman -Syu --noconfirm {{package}}`

- [s]earch the package database for a `regex` or keyword:

`pacman -Ss "{{search_pattern}}"`

- Display [i]nformation about a package:

`pacman -Si {{package}}`

- Overwrite conflicting files during a package update:

`sudo pacman -Syu --overwrite {{path/to/file}}`

- Remove not installed packages and unused repositories from the cache (use the flags `Scc` to [c]lean all packages):

`sudo pacman -Sc`

- Specify the package version that should be installed:

`sudo pacman -S {{package}}={{version}}`
