# elfedit

> Update the ELF header and program properties of ELF files.
> More information: <https://manned.org/elfedit>.

- Change the ELF machine type for files matching a specific input machine type:

`elfedit --input-mach x86-64 --output-mach i386 {{path/to/file}}`

- Change an ELF file type from a shared object to an executable:

`elfedit --input-type dyn --output-type exec {{path/to/file}}`

- Set the OSABI field in an ELF header:

`elfedit --output-osabi GNU {{path/to/file}}`

- Set the ABI version in an ELF header (the value must be between 0 and 255):

`elfedit --output-abiversion {{version}} {{path/to/file}}`

- Enable or disable an x86 program property:

`elfedit {{--enable-x86-feature|--disable-x86-feature}} {{ibt|shstk|lam_u48|lam_u57}} {{path/to/file}}`

- Display help:

`elfedit --help`

- Display version information:

`elfedit --version`
