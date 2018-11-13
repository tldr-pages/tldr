# ar

> Create, modify, and extract from archives (.a, .so, .o).

- Extract all members from an archive:

`ar -x {{libfoo.a}}`

- List the members of an archive:

`ar -t {{libfoo.a}}`

- Replace or add files to an archive:

`ar -r {{libfoo.a}} {{foo.o}} {{bar.o}} {{baz.o}}`

- Insert an object file index (equivalent to using `ranlib`):

`ar -s {{libfoo.a}}`

- Create an archive with files and an accompanying object file index:

`ar -rs {{libfoo.a}} {{foo.o}} {{bar.o}} {{baz.o}}`
