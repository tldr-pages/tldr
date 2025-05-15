# xml canonic

> Make XML documents canonical.
> More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139560880>.

- Make an XML document canonical, preserving comments:

`xml {{[c14n|canonic]}} {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- Make an XML document canonical, removing comments:

`xml {{[c14n|canonic]}} --without-comments {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- Make XML exclusively canonical, using an XPATH from a file, preserving comments:

`xml {{[c14n|canonic]}} --exc-with-comments {{path/to/input.xml|URI}} {{path/to/c14n.xpath}}`

- Display help:

`xml {{[c14n|canonic]}} --help`
