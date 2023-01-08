# pacman

> Arch Linux package manager utility.
> Some subcommands such as `pacman sync` have their own usage documentation.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Synchronize and update all packages:

`sudo pacman --sync --refresh --sysupgrade`
`sudo pacman -Syu`

- Install a new package:

`sudo pacman --sync {{package_name}}`
`sudo pacman -S {{package_name}}`

- Remove a package and its dependencies:

`sudo pacman --remove --recursive {{package_name}}`
`sudo pacman -Rs {{package_name}}`

- Search the package database for a regular expression or keyword:

`pacman --sync --search "{{search_pattern}}"`
`pacman -Ss "{{search_pattern}}"`

- List installed packages and versions:

`pacman --query`
`pacman -Q`

- List only the explicitly installed packages and versions:

`pacman --query --explicit`
`pacman -Qe`

- List orphan packages (installed as dependencies but not actually required by any package):

`pacman --query --unrequired --deps --quiet`
`pacman -Qtdq`

- Empty the entire pacman cache:

`sudo pacman --sync --clean --clean`
`sudo pacman -Scc`
