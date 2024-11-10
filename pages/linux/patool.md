# patool

> Patool is an archive file manager. Various archive formats can be created,
> extracted, tested, listed, searched, repacked and compared with patool.
> More information: <https://github.com/wummel/patool>.

- extract an archive:

`patool extract $ARCHIVE`

- list contents of an archive:

`patool list $ARCHIVE`

- run diff on contents of two archives and print to stdout:

`patool diff $ARCHIVE1 $ARCHIVE2`

- search for a string inside the contents of an archive:

`patool search $ARCHIVE`
