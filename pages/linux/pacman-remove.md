# pacman --remove

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Remove a package and its dependencies recursively:

`sudo pacman {{[-Rs|--remove --recursive]}} {{package}}`

- Remove a package and its dependencies. Also do not save backups of configuration files:

`sudo pacman {{[-Rsn|--remove --recursive --nosave]}} {{package}}`

- Remove a package without prompting:

`sudo pacman {{[-R|--remove]}} --noconfirm {{package}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`sudo pacman {{[-Rsn|--remove --recursive --nosave]}} $(pacman {{[-Qdtq|--query --deps --unrequired --quiet]}})`

- Remove a package and cascade that to all packages that depend on it:

`sudo pacman {{[-Rc|--remove --cascade]}} {{package}}`

- List and print packages that would be affected (does not remove any packages):

`pacman {{[-Rp|--remove --print]}} {{package}}`

- Display help:

`pacman {{[-Rh|--remove --help]}}`
