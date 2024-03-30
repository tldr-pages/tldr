# debuild

> Build a Debian package from source.
> More information: <https://manpages.debian.org/latest/devscripts/debuild.1.en.html>.

- Build the package in the current directory:

`debuild`

- Build a binary package only:

`debuild -b`

- Do not run lintian after building the package:

`debuild --no-lintian`
