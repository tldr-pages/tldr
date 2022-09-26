# pacman

> Arch Linux package manager utility.
> Some subcommands such as `pacman sync` have their own usage documentation.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Synchronize and update all packages:

`sudo pacman -Syu`

- Install a new package:

`sudo pacman -S {{package_name}}`

- Remove a package and its dependencies:

`sudo pacman -Rs {{package_name}}`

- Search the package database for a regular expression or keyword:

`pacman -Ss "{{search_pattern}}"`

- List installed packages and versions:

`pacman -Q`

- List only the explicitly installed packages and versions:

`pacman -Qe`

- List orphan packages (installed as dependencies but not actually required by any package):

`pacman -Qtdq`

- Empty the entire pacman cache:

`sudo pacman -Scc`
