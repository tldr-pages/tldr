# makepkg

> Create a package which can be used with `pacman`.
> Uses the `PKGBUILD` file in the current working directory by default.
> More information: <https://manned.org/makepkg>.

- Make a package:

`makepkg`

- Make a package and install its dependencies:

`makepkg {{[-s|--syncdeps]}}`

- Make a package, install its dependencies then install it to the system:

`makepkg {{[-si|--syncdeps --install]}}`

- Make a package, but skip checking the source's hashes:

`makepkg --skipchecksums`

- Clean up work directories after a successful build:

`makepkg {{[-c|--clean]}}`

- Verify the hashes of the sources:

`makepkg --verifysource`

- Generate and save the source information into `.SRCINFO`:

`makepkg --printsrcinfo > .SRCINFO`

- Download the source and install only the build dependencies for a program:

`makepkg {{[-so|--syncdeps --nobuild]}}`
