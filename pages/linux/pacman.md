# pacman

> Arch Linux package manager utility.
> See also: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Synchronize and update all packages:

`sudo pacman -Syu`

- Install a new package:

`sudo pacman -S {{package}}`

- Remove a package and its dependencies:

`sudo pacman -Rs {{package}}`

- Search the database for packages containing a specific file:

`pacman -F "{{file_name}}"`

- List installed packages and versions:

`pacman -Q`

- List only the explicitly installed packages and versions:

`pacman -Qe`

- List orphan packages (installed as dependencies but not actually required by any package):

`pacman -Qtdq`

- Empty the entire pacman cache:

`sudo pacman -Scc`
