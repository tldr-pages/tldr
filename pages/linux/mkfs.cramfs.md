# mkfs.cramfs

> Create a ROM filesystem inside a partition.
> More information: <https://manned.org/mkfs.cramfs>.

- Create a ROM filesystem out of a directory inside partition Y on device X:

`sudo mkfs.cramfs {{path/to/directory}} {{/dev/sdXY}}`

- Create a ROM filesystem with a volume-name:

`sudo mkfs.cramfs -n {{volume_name}} {{path/to/directory}} {{/dev/sdXY}}`
