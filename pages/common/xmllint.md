# xmllint

> XML parser and linter that supports XPath, a syntax for navigating XML trees.
> More information: <https://manned.org/xmllint>.

- Return all nodes (tags) named "foo":

`xmllint --xpath "//{{foo}}" {{path/to/file.xml}}`

- Return the contents of the first node named "foo" as a string:

`xmllint --xpath "string(//{{foo}})" {{path/to/file.xml}}`

- Return the href attribute of the second anchor element in an HTML file:

`xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml`

- Return human-readable (indented) XML from file:

`xmllint --format {{path/to/file.xml}}`

- Check that an XML file meets the requirements of its DOCTYPE declaration:

`xmllint --valid {{path/to/file.xml}}`

- Validate XML against DTD schema hosted online:

`xmllint --dtdvalid {{URL}} {{path/to/file.xml}}`
