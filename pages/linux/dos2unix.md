# dos2unix

> DOS/Mac to UNIX and vice versa text file format converter.

- Convert a file in the DOS format to the UNIX format:

`dos2unix {{filename}}`

- Convert DOS file format to UNIX format:

`unix2dos {{filename}}`

- Convert and replace a file while keeping original date stamp:

`unix2dos -k {{filename}}`

- Convert from DOS to UNIX format and write to a newfile:

`unix2dos -k {{input filename}} {{output filename}}`

- Suppress all warning and messages while conversion:

`dos2unix -q {{filename}}`
