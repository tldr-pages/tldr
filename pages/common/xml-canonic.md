# xml canonic

> Make XML documents canonical.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Make an XML document canonical, preserving comments:

`xml canonic {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- Make an XML document canonical, removing comments:

`xml canonic --without-comments {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- Make XML exclusively canonical, using an XPATH from a file, preserving comments:

`xml canonic --exc-with-comments {{path/to/input.xml|URI}} {{path/to/c14n.xpath}}`

- Display help:

`xml canonic --help`
