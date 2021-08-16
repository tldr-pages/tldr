# xml validate

> Validate XML documents.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Validate XML document(s) for well-formedness only (default behavior):

`xml validate --well-formed {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Validate XML document(s) against a Document Type Definition (DTD):

`xml validate --dtd {{path/to/schema.dtd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Validate XML document(s) against an XML Schema Definition (XSD):

`xml validate --xsd {{path/to/schema.xsd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Validate XML document(s) against a Relax NG schema (RNG):

`xml validate --relaxng {{path/to/schema.rng}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Display help for the `validate` subcommand:

`xml validate --help`
