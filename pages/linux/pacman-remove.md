# pacman --remove

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Remove a package and its dependencies:

`sudo pacman -Rs {{package}}`

- Remove a package and both its dependencies and configuration files:

`sudo pacman -Rs -n {{package}}`

- Remove a package without prompting:

`sudo pacman -R --noconfirm {{package}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`sudo pacman -R -n $(pacman -Qdtq)`

- Remove a package and all packages that depend on it:

`sudo pacman -Rc {{package}}`

- List packages that would be affected (does not remove any packages):

`pacman -Rp {{package}}`

- Display help:

`pacman -Rh`
