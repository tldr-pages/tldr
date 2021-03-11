# pkgfile

> Tool for searching files from packages in the official repositories on arch-based systems.
> See also `pacman files`.
> More information: <https://wiki.archlinux.org/index.php/Pkgfile>.

- Synchronize the pkgfile database:

`pkgfile -u`

- Search for a package that owns a specific file:

`pkgfile {{path/to/file}}`

- List all files provided by a package:

`pkgfile -l {{pagkage_name}}`
