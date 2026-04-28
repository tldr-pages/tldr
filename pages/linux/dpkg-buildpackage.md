# dpkg-buildpackage

> Compile binary and/or source Debian packages from source code.
> Normally executed inside a source tree that contains a `debian/` directory.
> Also handles build dependencies, creates files like `.buildinfo` and `.changes`, and signs the result if applicable.
> More information: <https://manned.org/dpkg-buildpackage>.

- Generate source and binary packages:

`dpkg-buildpackage`

- Generate only binary packages (no source package):

`dpkg-buildpackage {{[-b|--build=binary]}}`

- Generate only the source package (without compiling binaries):

`dpkg-buildpackage {{[-S|--build=source]}}`

- Do not sign the `.dsc` and `.changes` files:

`dpkg-buildpackage {{[-us|--unsigned-source]}} {{[-uc|--unsigned-changes]}}`

- Do not run `clean` before compiling:

`dpkg-buildpackage {{[-nc|--no-pre-clean]}}`

- Use `fakeroot` as the command to gain root privileges during the build:

`dpkg-buildpackage {{[-r|--root-command=]}}fakeroot`

- Run a specific `debian/rules` target:

`dpkg-buildpackage {{[-T|--rules-target=]}}{{clean}}`
