# dpkg-buildpackage

> Compile binary and/or source Debian packages from source code.
> Normally executed inside a source tree that contains a `debian/` directory.
> Also handles build dependencies, creates files like `.buildinfo` and `.changes`, and signs the result if applicable.
> More information: <https://man7.org/linux/man-pages/man1/dpkg-buildpackage.1.html>.

- Generate source and binary packages:

`dpkg-buildpackage`

- Generate only binary packages (no source package):

`dpkg-buildpackage -b`

- Generate only the source package (without compiling binaries):

`dpkg-buildpackage -S`

- Do not sign the `.dsc` and `.changes` files:

`dpkg-buildpackage -us -uc`

- Also do not sign the `.buildinfo` file:

`dpkg-buildpackage -us -uc -ui`

- Do not run `clean` before compiling:

`dpkg-buildpackage -nc`

- Also run `clean` after compilation:

`dpkg-buildpackage -tc`

- Do not check build dependencies:

`dpkg-buildpackage -d`

- Use `fakeroot` as the command to gain root privileges during the build:

`dpkg-buildpackage -rfakeroot`

- Run a specific `debian/rules` target:

`dpkg-buildpackage -T clean`

- Compile in parallel:

`DEB_BUILD_OPTIONS=parallel={{N}} dpkg-buildpackage`
