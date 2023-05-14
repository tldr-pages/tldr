# mksquashfs

> Create or append files and directories to squashfs filesystems.
> More information: <https://manned.org/mksquashfs>.

- Create or append files and directories to a squashfs filesystem (compressed using `gzip` by default):

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}}`

- Create or append files and directories to a squashfs filesystem, using a specific [comp]ression algorithm:

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -comp {{gzip|lzo|lz4|xz|zstd|lzma}}`

- Create or append files and directories to a squashfs filesystem, [e]xcluding some of them:

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -e {{file|directory1 file|directory2 ...}}`

- Create or append files and directories to a squashfs filesystem, [e]xcluding those ending with `.gz`:

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -wildcards -e "{{*.gz}}"`

- Create or append files and directories to a squashfs filesystem, [e]xcluding those matching a regular expression:

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -regex -e "{{regular_expression}}"`
