# patool

> Archive file manager.
> Various archive formats can be created, extracted, tested, listed, searched, repacked, and compared.
> More information: <https://github.com/wummel/patool>.

- Extract an archive:

`patool extract {{path/to/archive}}`

- Create an archive:

`patool create {{path/to/archive}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- List contents of an archive:

`patool list {{path/to/archive}}`

- Compare the contents of two archives and display the differences in `stdout`:

`patool diff {{path/to/archive1}} {{path/to/archive2}}`

- Search for a string inside the contents of an archive:

`patool search {{path/to/archive}}`
