# fallocate

> Reserve or deallocate disk space to files.
> The utility allocates space without zeroing.
> More information: <https://manned.org/fallocate>.

- Reserve a file taking up 700 MiB of disk space:

`fallocate --length {{700M}} {{path/to/file}}`

- Shrink an already allocated file by 200 MiB:

`fallocate --collapse-range --length {{200M}} {{path/to/file}}`

- Shrink 20 MB of space after 100 MiB in a file:

`fallocate --collapse-range --offset {{100M}} --length {{20M}} {{path/to/file}}`
