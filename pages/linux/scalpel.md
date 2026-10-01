# scalpel

> Recover files from a disk image based on file headers and footers.
> File patterns must be enabled in the configuration file (all are commented out by default).
> More information: <https://manned.org/scalpel>.

- Carve files from a disk image using a specific configuration file:

`scalpel -c {{path/to/scalpel.conf}} -o {{path/to/output_directory}} {{path/to/disk_image.dd}}`

- Preview which files would be carved, without actually carving them:

`scalpel -p -c {{path/to/scalpel.conf}} -o {{path/to/output_directory}} {{path/to/disk_image.dd}}`

- Skip the first N bytes of the disk image before carving:

`scalpel -s {{number}} -c {{path/to/scalpel.conf}} -o {{path/to/output_directory}} {{path/to/disk_image.dd}}`

- Carve files without organizing them into subdirectories by type:

`scalpel -O -c {{path/to/scalpel.conf}} -o {{path/to/output_directory}} {{path/to/disk_image.dd}}`

- Display help:

`scalpel -h`

- Display version:

`scalpel -V`
