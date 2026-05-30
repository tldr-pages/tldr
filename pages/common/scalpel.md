# scalpel

> Recover files from a disk image or raw block device based on file headers and footers.
> More information: <https://manpages.ubuntu.com/manpages/jammy/man1/scalpel.1.html>.

- Recover files from a disk image:

`scalpel {{path/to/disk_image}}`

- Use a specific configuration file:

`scalpel -c {{path/to/scalpel.conf}} {{path/to/disk_image}}`

- Save recovered files to a specific output directory:

`scalpel -o {{path/to/output_directory}} {{path/to/disk_image}}`

- Preview which files would be recovered without actually carving them:

`scalpel -p {{path/to/disk_image}}`

- Read a list of input files from a file:

`scalpel -i {{path/to/input_file_list}}`
