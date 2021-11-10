# install

> Copy files and set attributes.
> Copy files (often executable) to a system location like `/usr/local/bin`, give them the appropriate permissions/ownership.
> More information: <https://www.gnu.org/software/coreutils/install>.

- Copy files to the destination:

`install {{path/to/source}} {{path/to/destination}}`

- Copy files to the destination, setting their ownership:

`install --owner {{user}} {{path/to/source}} {{path/to/destination}}`

- Copy files to the destination, setting their group ownership:

`install --group {{user}} {{path/to/source}} {{path/to/destination}}`

- Copy files to the destination, setting their `mode`:

`install --mode {{+x}} {{path/to/source}} {{path/to/destination}}`

- Copy files and apply access/modification times of source to the destination:

`install --preserve-timestamps {{path/to/source}} {{path/to/destination}}`
