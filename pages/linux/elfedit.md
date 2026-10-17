# elfedit

> Update the ELF header and program property of ELF files.
> More information: <https://sourceware.org/binutils/docs/binutils/elfedit.html>.

- Change the ELF machine architecture:

`elfedit --output-mach={{i386|x86-64|IAMCU}} {{path/to/binary}}`

- Change the ELF file type:

`elfedit --output-type={{exec|dyn|rel}} {{path/to/binary}}`

- Change the target OS ABI:

`elfedit --output-osabi={{none|HPUX|NetBSD|GNU|Linux|Solaris|FreeBSD|OpenBSD}} {{path/to/binary}}`

- Change the ELF ABI version:

`elfedit --output-abiversion={{0}} {{path/to/binary}}`

- Enable an x86 program property feature:

`elfedit --enable-x86-feature={{ibt|shstk|lam_u48|lam_u57}} {{path/to/binary}}`

- Disable an x86 program property feature:

`elfedit --disable-x86-feature={{ibt|shstk}} {{path/to/binary}}`

- Only update files matching a specific input machine type:

`elfedit --input-mach={{i386}} --output-mach={{x86-64}} {{path/to/binary}}`

- Display help:

`elfedit --help`
