# foremost

> Recover files using their headers, footers, and data structures.
> More information: <https://manned.org/foremost>.

- Recover files of a specific [t]ype (e.g., JPEG) from a disk image:

`foremost -t {{jpg}} -i {{path/to/disk_image.dd}}`

- Recover files of multiple types:

`foremost -t {{gif,png,pdf}} -i {{path/to/disk_image.dd}}`

- Recover files using all predefined formats:

`foremost -t all -i {{path/to/disk_image.dd}}`

- Recover files into a specific output directory:

`foremost -o {{path/to/output_directory}} -i {{path/to/disk_image.dd}}`

- Display [h]elp:

`foremost -h`

- Display [V]ersion:

`foremost -V`
