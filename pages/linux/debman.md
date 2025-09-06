# debman

> Read man pages from uninstalled packages.
> More information: <https://manned.org/debman.1>.

- Read a man page for a command that is provided by a specified [p]ackage:

`debman -p {{package}} {{command}}`

- Specify a [p]ackage version to download:

`debman -p {{package}}={{version}} {{command}}`

- Read a man page in a `.deb` [f]ile:

`debman -f {{path/to/filename.deb}} {{command}}`
