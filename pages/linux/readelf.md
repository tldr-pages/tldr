# readelf

> Display information about ELF files.
> More information: <https://manned.org/readelf>.

- Display all information about the ELF file:

`readelf {{[-a|--all]}} {{path/to/binary}}`

- Display all the headers present in the ELF file:

`readelf {{[-e|--headers]}} {{path/to/binary}}`

- Display the entries in symbol table section of the ELF file, if it has one:

`readelf {{[-s|--symbols]}} {{path/to/binary}}`

- Display ELF header information:

`readelf {{[-h|--file-header]}} {{path/to/binary}}`

- Display ELF section header information:

`readelf {{[-S|--section-headers]}} {{path/to/binary}}`

- Display DWARF information:

`readelf {{[-w|--debug-dump]}} {{path/to/binary}}`
