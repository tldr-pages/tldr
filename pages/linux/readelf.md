# readelf

> Display information about ELF files.
> More information: <http://man7.org/linux/man-pages/man1/readelf.1.html>.

- Display all information about the ELF file:

`readelf -all {{path/to/binary}}`

- Display all the headers present in the ELF file:

`readelf --headers {{path/to/binary}}`

- Display the entries in symbol table section of the ELF file, if it has one:

`readelf --symbols {{path/to/binary}}`

- Display the information contained in the ELF header at the start of the file:

`readelf --file-header {{path/to/binary}}`
