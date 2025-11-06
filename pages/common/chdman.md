# chdman

> Manage and convert CHD (Compressed Hunks of Data) images.
> Commonly used with MAME and retro game images.
> More information: <https://docs.mamedev.org/tools/chdman.html>.

- Create a CHD from a BIN/CUE pair (CD-ROM image):

`chdman createcd -i {{path/to/file.cue}} -o {{path/to/file.chd}}`

- Create a CHD from a raw hard drive image:

`chdman createhd -i {{path/to/disk.img}} -o {{path/to/disk.chd}}`

- Extract (decompress) a CHD back to BIN/CUE:

`chdman extractcd -i {{path/to/file.chd}} -o {{path/to/file.cue}}`

- Verify integrity of CHD file:

`chdman verif -i {{path/to/file.chd}}`

- View CHD metadata information:

`chdman info -i {{path/to/file.chd}}`

- Update a CHD file to the latest format version:

`chdman copy -i {{path/to/old_file.chd}} -o {{path/to/new_file.chd}}`

- Convert a compressed hard drive image to uncompressed (for editing):

`chdman extracthd -i {{path/to/disk.chd}} -o {{path/to/disk.img}}`
