# xml-validate

> XMLStarlet toolkit: Validate XML documents.
> More information: <http://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Validate XML document for well-formedness only (default):

`xml validate --well-formed {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Validate XML document against Document Type Definition (DTD):

`xml validate --dtd {{path/to/schema.dtd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Validate XML document against XML Schema Definition (XSD):

`xml validate --xsd {{path/to/schema.xsd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Validate XML document against a Relax NG schema (RNG):

`xml validate --relaxng {{path/to/schema.rng}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Display help for `validate` subcommand:

`xml validate --help`
