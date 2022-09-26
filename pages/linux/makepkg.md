# makepkg

> Create a package which can be used with `pacman`.
> Uses the `PKGBUILD` file in the current working directory by default.
> More information: <https://man.archlinux.org/man/makepkg.8>.

- Make a package:

`makepkg`

- Make a package and install its dependencies:

`makepkg --syncdeps`

- Make a package, install its dependencies then install it to the system:

`makepkg --syncdeps --install`

- Make a package, but skip checking the source's hashes:

`makepkg --skipchecksums`

- Clean up work directories after a successful build:

`makepkg --clean`

- Verify the hashes of the sources:

`makepkg --verifysource`

- Generate and save the source information into `.SRCINFO`:

`makepkg --printsrcinfo > .SRCINFO`
