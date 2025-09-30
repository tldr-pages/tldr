# kpartx

> Create device maps from partition tables.
> More information: <https://manned.org/kpartx>.

- Add partition mappings and print created mappings:

`kpartx -av {{whole_disk.img}}`

- Delete partition mappings:

`kpartx -d {{whole_disk.img}}`

- List partition mappings:

`kpartx -l {{whole_disk.img}}`
