# pacman

> Arch Linux package manager utility.
> See also: `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://manned.org/pacman.8>.

- Synchronize and update all packages:

`sudo pacman {{[-Syu|--sync --refresh --sysupgrade]}}`

- Install a new package:

`sudo pacman {{[-S|--sync]}} {{package}}`

- Remove a package and its dependencies:

`sudo pacman {{[-Rs|--remove --recursive]}} {{package}}`

- Search the package database for a regular expression or keyword:

`pacman {{[-Ss|--sync --search]}} "{{search_pattern}}"`

- Search the database for packages containing a specific file:

`pacman {{[-F|--files]}} "{{file_name}}"`

- List only the explicitly installed packages and versions:

`pacman {{[-Qe|--query --explicit]}}`

- List orphan packages (installed as dependencies but not actually required by any package):

`pacman {{[-Qdtq|--query --deps --unrequired --quiet]}}`

- Empty the entire `pacman` cache:

`sudo pacman {{[-Scc|--sync --clean --clean]}}`
