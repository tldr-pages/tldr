# dget

> Download Debian packages.
> More information: <https://manned.org/dget.1>.

- Download a binary package:

`dget {{package}}`

- Download and extract a package source from its `.dsc` file:

`dget {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`

- Download a package source tarball from its `.dsc` file but don't extract it:

`dget {{[-d|--download-only]}} {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`
