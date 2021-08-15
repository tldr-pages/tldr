# xml-canonic

> Make XML documents canonical.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Make an XML document canonical, including comments (default):

`xml canonic --with-comments {{path/to/input.xml|URI}} >{{path/to/output.xml}}`

- Make an XML document canonical, without comments:

`xml canonic --without-comments {{path/to/input.xml|URI}} >{{path/to/output.xml}}`

- Exclusive XML canonicalization, using an XPATH from a file:

`xml canonic --exc-with-comments {{path/to/input.xml|URI}} {{path/to/c14n.xpath}}`

- Display help for `canonic` subcommand:

`xml canonic --help`
