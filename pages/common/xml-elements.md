# xml elements

> Extract elements and display structure of an XML document.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Extract elements from an XML document (producing XPATH expressions):

`xml elements {{path/to/input.xml|URI}} >{{path/to/elements}}`

- Extract elements and attributes from an XML document:

`xml elements -a {{path/to/input.xml|URI}} >{{path/to/elements}}`

- Extract elements, attributes, and their values from an XML doc:

`xml elements -v {{path/to/input.xml|URI}} >{{path/to/elements}}`

- Print sorted unique elements from an XML document (to see structure):

`xml elements -u {{path/to/input.xml|URI}}`

- Print sorted unique elements up to a depth of 3:

`xml elements -d{{3}} {{path/to/input.xml|URI}}`

- Display help for the `elements` subcommand:

`xml elements --help`
