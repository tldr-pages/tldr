# makepkg

> Creates a package installable with the `pacman` package manager.
> Runs the commands specified in a PKGBUILD file to build the package. Read more at https://wiki.archlinux.org/index.php/Makepkg

- Make a package (run in the same directory as a PKGBUILD):

`makepkg`

- Make a package and install its dependencies (specified in the PKGBUILD):

`makepkg --syncdeps`

- The same as above, but install the package with `pacman` when done:

`makepkg --syncdeps --install`
 
- Make a package but skip source checksums (also specified in the PKGBUILD):
 
`makepkg --skipchecksums`
