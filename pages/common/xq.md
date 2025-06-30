# xq

> A lightweight XML and HTML formatting and querying tool.
> See also: `xmlstarlet`
> More information: <https://github.com/sibprogrammer/xq>.

- Format an XML file and highlight the syntax:

`xq {{path/to/file.xml}}`

- Read input from stdin and format it as XML or HTML:

`curl -s {{url}} | xq`

- Format HT[M]L content and highlight the syntax:

`xq {{-m|--html}} {{path/to/file.html}}`

- E[x]tract the text content of all nodes with a specific name from an XML file:

`xq {{-x|--xpath}} //{{node_name}} {{path/to/file.xml}}`

- E[x]tract the XML content of all [n]odes with a specific name from an XML file:

`xq {{-n|--node}} {{-x|--xpath}} //{{node_name}} {{path/to/file.xml}}`

- Convert an XML file to a [J]SON-formatted array:

`xq {{-j|--json}} {{path/to/file.xml}}`
