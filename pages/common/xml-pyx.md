# xml pyx

> Convert an XML document to PYX (ESIS - ISO 8879) format.
> More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>.

- Convert an XML document to PYX format:

`xml pyx {{path/to/input.xml|URI}} > {{path/to/output.pyx}}`

- Convert an XML document from `stdin` to PYX format:

`cat {{path/to/input.xml}} | xml pyx > {{path/to/output.pyx}}`

- Display help:

`xml pyx --help`
