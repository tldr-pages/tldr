# pkgit

> package it!
> install programs from their git repo
> More information: <https://git.symlinx.net/pkgit>

- Install a package from a git repo:

`pkgit {{[-i|--install]}} [url.git]`

- Install a package defined in your configuration file

`pkgit {{[-i|--install]}} [pkg_name]`

- Install all packages declared in your configuration file

`pkgit {{[-d|--declare]}}`

- Remove a package:

`pkgit {{[-r|--remove]}} [pkg_name]`

- Update installed packages:

`pkgit {{[-u|--update]}}`

- Add a repository to your configuration file

`pkgit {{[-a|--add]}} [url.git]`

- Autodetect a build system and build a project

`pkgit {{[-b|--build]}} [path]`
