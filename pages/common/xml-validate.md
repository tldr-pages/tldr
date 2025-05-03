# xml validate

> Validate XML documents.
> More information: <https://xmlstar.sourceforge.net/docs.php>.

- Validate one or more XML documents for well-formedness only:

`xml validate {{path/to/input1.xml|URI1 path/to/input2.xml|URI2 ...}}`

- Validate one or more XML documents against a Document Type Definition (DTD):

`xml validate --dtd {{path/to/schema.dtd}} {{path/to/input1.xml|URI1 path/to/input2.xml|URI2 ...}}`

- Validate one or more XML documents against an XML Schema Definition (XSD):

`xml validate --xsd {{path/to/schema.xsd}} {{path/to/input1.xml|URI1 path/to/input2.xml|URI2 ...}}`

- Validate one or more XML documents against a Relax NG schema (RNG):

`xml validate --relaxng {{path/to/schema.rng}} {{path/to/input1.xml|URI1 path/to/input2.xml|URI2 ...}}`

- Display help:

`xml validate --help`
