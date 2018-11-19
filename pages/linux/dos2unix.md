# dos2unix

> DOS/Mac to UNIX and vice versa text file format converter.
> Also check unix2dos

- Convert a file in the DOS format to the UNIX format:

`dos2unix {{path/to/file}}`

- Convert and replace a file while keeping original date stamp:

`dos2unix -k {{filename}}`

- Convert from DOS to UNIX format and write to a newfile:

`dos2unix -k {{input filename}} {{output filename}}`

- Suppress all warning and messages while conversion:

`dos2unix -q {{filename}}`
