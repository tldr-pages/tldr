# daps

> An open source program for transforming DocBook XML into output formats such as HTML or PDF.
> More information: <https://opensuse.github.io/daps/doc/index.html>.

- Check if a DocBook XML file is valid:

`daps -d {{path/to/file.xml}} validate`

- Convert a DocBook XML file into PDF:

`daps -d {{path/to/file.xml}} pdf`

- Convert a DocBook XML file into a single HTML file:

`daps -d {{path/to/file.xml}} html --single`

- Display help:

`daps --help`

- Display version:

`daps --version`
