# shelly

> A modern, unified package manager for Arch Linux.
> See also: `pacman`, `paru`, `yay`.
> More information: <https://www.seafoam-labs.org/shelly-alpm/docs/cli-reference/>.

- Upgrade all packages from every source (repo, AUR, Flatpak, AppImage):

`shelly upgrade-all`

- Install a package:

`shelly install {{package}}`

- Remove an installed package and its orphaned dependencies:

`shelly remove --cascade {{package}}`

- Search for a package in the standard repositories:

`shelly query --available {{search_term}}`

- Search for a package specifically in the AUR:

`shelly aur search {{search_term}}`

- Remove orphaned packages (installed as dependencies but no longer required):

`shelly purify --orphans`
