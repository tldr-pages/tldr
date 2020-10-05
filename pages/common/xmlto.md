# xmlto

> Apply an XSL stylesheet to an XML document.
> More information: <https://pagure.io/xmlto>.

- Convert a DocBook XML document to PDF format:

`xmlto {{pdf}} {{document.xml}}`

- Convert a DocBook XML document to HTML format and store the resulting files in a separate directory:

`xmlto -o {{path/to/html_files}} {{html}} {{document.xml}}`

- Convert a DocBook XML document to a single HTML file:

`xmlto {{html-nochunks}} {{document.xml}}`

- Specify a stylesheet to use while converting a DocBook XML document:

`xmlto -x {{stylesheet.xsl}} {{output-format}} {{document.xml}}`
