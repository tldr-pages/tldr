# pkgmk

> Make a binary package for use with pkgadd on CRUX.
> More information: <https://docs.oracle.com/cd/E19683-01/816-0210/6m6nb7mha/index.html>.

- Make and download a package:

`pkgmk -d`

- Install the package after making it:

`pkgmk -d -i`

- Upgrade the package after making it:

`pkgmk -d -u`

- Ignore the footprint when making a package:

`pkgmk -d -if`

- Ignore the MD5 sum when making a package:

`pkgmk -d -im`

- Update the package's footprint:

`pkgmk -uf`
