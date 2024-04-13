# eu-readelf

> Displays information about ELF files.
> More information: <https://manned.org/eu-readelf>.

- Display all extractable information contained in the ELF file:

`eu-readelf --all {{path/to/file}}`

- Display the contents of all NOTE segments/sections, or of a particular segment/section:

`eu-readelf --notes[={{.note.ABI-tag}}] {{path/to/file}}`
