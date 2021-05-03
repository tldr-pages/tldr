# ar

> Create, modify, and extract from archives (`.a`, `.so`, `.o`).
> More information: <https://manned.org/ar>.

- Extract all members from an archive:

`ar -x {{path/to/file.a}}`

- List the members of an archive:

`ar -t {{path/to/file.a}}`

- Replace or add files to an archive:

`ar -r {{path/to/file.a}} {{path/to/file1.o}} {{path/to/file2.o}}`

- Insert an object file index (equivalent to using `ranlib`):

`ar -s {{path/to/file.a}}`

- Create an archive with files and an accompanying object file index:

`ar -rs {{path/to/file.a}} {{path/to/file1.o}} {{path/to/file2.o}}`
