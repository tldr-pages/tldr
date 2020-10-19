# debuild

> Tool to build a Debian package from source.
> More information: <https://manpages.debian.org/debuild>.

- Build the package in the current directory:

`debuild`

- Build a binary package only:

`debuild -b`

- Do not run lintian after building the package:

`debuild --no-lintian`
