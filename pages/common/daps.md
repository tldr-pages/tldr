# daps

> DAPS is an open source program for transforming DocBook XML into output formats such as HTML or PDF.
> More information: <https://opensuse.github.io/daps/doc/index.html>.

- Check your DocBook XML file is vaild:

`daps -d {{path/to/docbook.xml}} validate`

- Convert your XML file into PDF:

`daps -d {{path/to/DC-file}} pdf`

- Convert your XML file into HTML:

`daps -d {{path/to/DC-file}} html --single`

- Display help:

`daps --help`

- Display version:

`daps --version`
