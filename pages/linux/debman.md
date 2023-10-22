# debman

> Read man pages from uninstalled packages.
> More information: <https://manpages.debian.org/latest/debian-goodies/debman.1.html>.

- Read a man page for a command that is provided by a specified package:

`debman -p {{package}} {{command}}`

- Specify a package version to download:

`debman -p {{package}}={{version}} {{command}}`

- Read a man page in a `.deb` file:

`debman -f {{path/to/filename.deb}} {{command}}`
