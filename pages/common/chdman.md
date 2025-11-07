# chdman

> Manage and convert CHD (Compressed Hunks of Data) images.
> Commonly used with MAME and retro game images.
> More information: <https://docs.mamedev.org/tools/chdman.html>.

- Create a CHD from a BIN/CUE pair (CD-ROM image):

`chdman createcd {{[-i|--input]}} {{path/to/file.cue}} {{[-o|--output]}} {{path/to/file.chd}}`

- Create a CHD from a raw hard drive image:

`chdman createhd {{[-i|--input]}} {{path/to/disk.img}} {{[-o|--output]}} {{path/to/disk.chd}}`

- Extract (decompress) a CHD back to BIN/CUE:

`chdman extractcd {{[-i|--input]}} {{path/to/file.chd}} {{[-o|--output]}} {{path/to/file.cue}}`

- Verify integrity of CHD file:

`chdman verif {{[-i|--input]}} {{path/to/file.chd}}`

- View CHD metadata information:

`chdman info {{[-i|--input]}} {{path/to/file.chd}}`

- Update a CHD file to the latest format version:

`chdman copy {{[-i|--input]}} {{path/to/old_file.chd}} {{[-o|--output]}} {{path/to/new_file.chd}}`

- Convert a compressed hard drive image to uncompressed (for editing):

`chdman extracthd {{[-i|--input]}} {{path/to/disk.chd}} {{[-o|--output]}} {{path/to/disk.img}}`
