# elfedit

> Update the ELF header and program properties of ELF files.
> See also: `readelf`, `objcopy`.
> More information: <https://manned.org/elfedit>.

- Change the machine type of an ELF file:

`elfedit --output-mach {{x86-64|i386|iamcu|...}} {{path/to/file}}`

- Change the machine type only in files that currently have a specific machine type:

`elfedit --input-mach {{i386}} --output-mach {{iamcu}} {{path/to/file1 path/to/file2 ...}}`

- Change the file type to relocatable, executable, or shared object:

`elfedit --output-type {{rel|exec|dyn}} {{path/to/file}}`

- Change the OSABI:

`elfedit --output-osabi {{none|Linux|FreeBSD|...}} {{path/to/file}}`

- Change the ABI version:

`elfedit --output-abiversion {{0..255}} {{path/to/file}}`

- Enable an x86 feature in an executable or shared library:

`elfedit --enable-x86-feature {{ibt|shstk|lam_u48|lam_u57}} {{path/to/file}}`

- Disable an x86 feature in an executable or shared library:

`elfedit --disable-x86-feature {{ibt|shstk|lam_u48|lam_u57}} {{path/to/file}}`

- Display help:

`elfedit {{[-h|--help]}}`
