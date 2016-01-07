# pkgmk

> Make a binary package for use with pkgadd on CRUX

- make and download a package

`pkgmk -d`

- install the package after making it

`pkgmk -d -i`

- upgrade the package after making it 

`pkgmk -d -u`

- ignore the footprint when making a package

`pkgmk -d -if`

- ignore the MD5 sum when making a package

`pkgmk -d -im`

- update the package's footprint

`pkgmk -uf`
