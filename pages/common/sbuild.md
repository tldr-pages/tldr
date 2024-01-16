# sbuild

> Build a Debian binary package in a clean `schroot`.
> More information: <https://wiki.debian.org/sbuild>.

- Build the package in the current directory:

`sbuild`

- Build the given package:

`sbuild {{package}}`

- Build for a certain distribution:

`sbuild --dist {{distribution}}`

- Build using custom dependencies:

`sbuild --extra-package={{path/to/deb/files}}`

- Run a shell in case of build failure to further investigate:

`sbuild --build-failed-commands=%SBUILD_SHELL`

- Cross build for a certain architecture:

`sbuild --host={{architecture}}`

- Build for the given native architecture:

`sbuild --arch={{architecture}}`
