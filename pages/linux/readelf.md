# readelf

> Display information about ELF files.
> More information: <https://manned.org/readelf.1>.

- Display all information about the ELF file:

`readelf -all {{path/to/binary}}`

- Display all the headers present in the ELF file:

`readelf --headers {{path/to/binary}}`

- Display the entries in symbol table section of the ELF file, if it has one:

`readelf --symbols {{path/to/binary}}`

- Display ELF header information:

`readelf --file-header {{path/to/binary}}`

- Display ELF section header information:

`readelf --section-headers {{path/to/binary}}`
