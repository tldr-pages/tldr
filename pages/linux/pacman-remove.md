# pacman --remove

> Remove packages from the system.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- [R]emove a package and its dependencies recur[s]ively:

`sudo pacman -Rs {{package}}`

- [R]emove a package and its dependencies. Also do [n]ot save backups of configuration files:

`sudo pacman -Rsn {{package}}`

- [R]emove a package without prompting:

`sudo pacman -R --noconfirm {{package}}`

- [R]emove orphan packages (installed as [d]ependencies but no[t] required by any package):

`sudo pacman -Rsn $(pacman -Qdtq)`

- [R]emove a package and [c]ascade that to all packages that depend on it:

`sudo pacman -Rc {{package}}`

- List and [p]rint packages that would be affected (does not [R]emove any packages):

`pacman -Rp {{package}}`

- Display [h]elp:

`pacman -Rh`
