# alien

> Converts different instalation packages to multiple other formats. 
> More information: http://manpages.ubuntu.com/manpages/trusty/man1/alien.1p.html.

- Convert a specific installation file to Debian format (`.deb extension):

`sudo alien --to-deb {{path/to/file}}`

- Convert a specific installation file to Red Hat format (`.rpm extension):

`sudo alien --to-rpm {{path/to/file}]`

- Convert a specific installation file to Stampede [SLP] format:

`sudo alien --to-slp {{path/to/file}}`

- Convert a specific installation file to a Slackware installation file (`.tgz extension`):

`sudo alien --to-tgz {{file}}`

- Convert a specific installation file to Debian format and install on the system:

`sudo alien --to-deb --install {{file}}`
