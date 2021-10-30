# alien

> Convert different installation packages to other formats.
> More information: <https://manned.org/alien>.

- Convert a specific installation file to Debian format (`.deb` extension):

`sudo alien --to-deb {{path/to/file}}`

- Convert a specific installation file to Red Hat format (`.rpm` extension):

`sudo alien --to-rpm {{path/to/file}}`

- Convert a specific installation file to a Slackware installation file (`.tgz` extension):

`sudo alien --to-tgz {{path/to/file}}`

- Convert a specific installation file to Debian format and install on the system:

`sudo alien --to-deb --install {{path/to/file}}`
