# ebuild

> A low level interface to the Gentoo Portage system.

- Create or update the package manifest:

`ebuild {{path/to/file.ebuild}} manifest`

- Clean the temporary build directories for the build file:

`ebuild {{path/to/file.ebuild}} clean`

- Fetch sources if they do not exist:

`ebuild {{path/to/file.ebuild}} fetch`

- Extract the sources to a temporary build directory:

`ebuild {{path/to/file.ebuild}} unpack`

- Compile the extracted sources:

`ebuild {{path/to/file.ebuild}} compile`

- Install the package to a temporary install directory:

`ebuild {{path/to/file.ebuild}} install`

- Install the temporary files to the live filesystem:

`ebuild {{path/to/file.ebuild}} qmerge`

- Fetch, unpack, compile, install and qmerge the specified ebuild file:

`ebuild {{path/to/file.ebuild}} merge`
