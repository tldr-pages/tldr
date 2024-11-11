# patool

> Patool is an archive file manager.
> Various archive formats can be created, extracted, tested, listed, searched, repacked and compared with patool.
> More information: <https://github.com/wummel/patool>.

- Extract an archive.:

`patool extract $ARCHIVE`

- List contents of an archive:

`patool list $ARCHIVE`

- Run diff on contents of two archives and print to stdout:

`patool diff $ARCHIVE1 $ARCHIVE2`

- Search for a string inside the contents of an archive:

`patool search $ARCHIVE`
