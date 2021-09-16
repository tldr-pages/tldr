# makepkg

> Creates a package installable with the `pacman` package manager.
> Runs the commands from a `PKGBUILD` file to build the package.
> More information: <https://man.archlinux.org/man/makepkg.8>.

- Make a package (run in the same directory as a `PKGBUILD`):

`makepkg`

- Make a package and install its dependencies:

`makepkg --syncdeps`

- Same as above, but install the package with `pacman` when done:

`makepkg --syncdeps --install`

- Make a package, but skip source checksums:

`makepkg --skipchecksums`

- Clean up work directories after a successful build:

`makepkg --clean`
