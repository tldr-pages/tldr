# xml-elements

> Extract elements and structure of an XML document.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Extract elements of an XML document (as XPATH expressions):

`xml elements {{path/to/input.xml|URI}} >{{path/to/elements}}`

- Extract elements and attributes of an XML document:

`xml elements -a {{path/to/input.xml|URI}} >{{path/to/elements}}`

- Extract elements, attributes, and their values:

`xml elements -v {{path/to/input.xml|URI}} >{{path/to/elements}}`

- Print sorted unique elements of an XML document (to see structure):

`xml elements -u {{path/to/input.xml|URI}}`

- Print sorted unique elements up to a depth of 3:

`xml elements -d{{3}} {{path/to/input.xml|URI}}`

- Display help for `elements` subcommand:

`xml elements --help`
