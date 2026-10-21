# elfedit

> Update the ELF header and program property of ELF files.
> More information: <https://manned.org/elfedit>.

- Change the machine type in the ELF header:

`elfedit --output-mach={{x86-64}} {{path/to/binary}}`

- Change the file type in the ELF header (`rel`, `exec` or `dyn`):

`elfedit --output-type={{type}} {{path/to/binary}}`

- Change the OS ABI in the ELF header (e.g. `none`, `GNU`, `FreeBSD`):

`elfedit --output-osabi={{osabi}} {{path/to/binary}}`

- Change the ABI version in the ELF header (between 0 and 255):

`elfedit --output-abiversion={{version}} {{path/to/binary}}`

- Enable an x86 feature (`ibt` or `shstk`) in the program property of an executable or shared object:

`elfedit --enable-x86-feature={{feature}} {{path/to/binary}}`

- Disable an x86 feature in the program property:

`elfedit --disable-x86-feature={{feature}} {{path/to/binary}}`

- Display version:

`elfedit --version`
