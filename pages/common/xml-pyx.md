# xml pyx

> Convert an XML document to PYX (ESIS - ISO 8879) format.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Convert an XML document to PYX format:

`xml pyx {{path/to/input.xml|URI}} > {{path/to/output.pyx}}`

- Convert an XML document from stdin to PYX format:

`cat {{path/to/input.xml}} | xml pyx > {{path/to/output.pyx}}`

- Display help for the `pyx` subcommand:

`xml pyx --help`
