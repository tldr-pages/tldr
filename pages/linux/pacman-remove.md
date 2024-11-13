# pacman --remove

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- [R]emove a package and its dependencies recursively ([s]):

`sudo pacman -Rs {{package}}`

- Remove a package and both its dependencies and configuration files ([n]):

`sudo pacman -Rs -n {{package}}`

- Remove a package without prompting:

`sudo pacman -R --noconfirm {{package}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`sudo pacman -Rs -n $(pacman -Qdtq)`

- Remove a package and all packages that depend on it:

`sudo pacman -Rc {{package}}`

- List and [p]rint packages that would be affected (does not remove any packages):

`pacman -Rp {{package}}`

- Display [h]elp:

`pacman -Rh`
