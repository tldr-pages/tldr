# xml

> Query, edit, check, convert, and transform XML documents.
> More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html>.

- Select nodes from an XML file using an XPath expression:

`xml sel -t -v "{{//xpath/expression}}" {{path/to/file.xml}}`

- Edit a node value in-place using an XPath expression:

`xml ed --inplace -u "{{//xpath/expression}}" -v "{{new_value}}" {{path/to/file.xml}}`

- Validate an XML file against an XSD schema:

`xml val --xsd {{path/to/schema.xsd}} {{path/to/file.xml}}`

- Pretty-print (indent) an XML file:

`xml fo {{path/to/file.xml}}`

- Transform an XML file using an XSLT stylesheet:

`xml tr {{path/to/stylesheet.xsl}} {{path/to/file.xml}}`

- Display help for a specific subcommand:

`xml {{sel|ed|val|fo|tr}} --help`
