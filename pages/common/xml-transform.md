# xml transform

> Transform XML documents using XSLT.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Transform an XML document using an XSL stylesheet, passing one XPATH parameter and one literal string parameter:

`xml transform {{path/to/stylesheet.xsl}} -p "{{Count='count(/xml/table/rec)'}}" -s {{Text="Count="}} {{path/to/input.xml|URI}}`

- Display help for the `transform` subcommand:

`xml transform --help`
