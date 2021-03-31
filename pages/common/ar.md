# ar

> Create, modify, and extract from archives (.a, .so, .o).
> More information: <https://man.archlinux.org/man/ar.1>.

- Extract all members from an archive:

`ar -x {{path/to/archive.a}}`

- List the members of an archive:

`ar -t {{path/to/archive.a}}`

- Replace or add files to an archive:

`ar -r {{path/to/archive.a}} {{path/to/file1.o}} {{path/to/file2.o}}`

- Insert an object file index (equivalent to using `ranlib`):

`ar -s {{path/to/archive.a}}`

- Create an archive with files and an accompanying object file index:

`ar -rs {{path/to/archive.a}} {{path/to/file1.o}} {{path/to/file2.o}}`
