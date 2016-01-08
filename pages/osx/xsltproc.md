# xsltproc

> Transform XML with XSLT to produce output (usually HTML or XML).

- Transform an XML file with a specific XSLT stylesheet:

`xsltproc --output {{output.html}} {{stylesheet.xslt}} {{xmlfile.xml}}`

- Pass a value to a parameter in the stylesheet:

`xsltproc --output {{output.html}} --stringparam {{name}} {{value}} {{stylesheet.xslt}} {{xmlfile.xml}}`
