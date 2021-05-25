# dget

> Download Debian packages.
> More information: <https://manpages.debian.org/dget>.

- Download a binary package:

`dget {{package_name}}`

- Download and extract a package source from its `.dsc` file:

`dget {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`

- Download a package source tarball from its `.dsc` file but don't extract it:

`dget -d {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`
