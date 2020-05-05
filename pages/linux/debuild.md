# debuild

> Tool to build a Debian package from source.
> More information: <https://manpages.debian.org/buster/devscripts/debuild.1.en.html>.

- Build the package in the current directory:

`debuild`

- Only build a binary package:

`debuild -b`

- Do not run lintian after building the package:

`debuild --no-lintian`
