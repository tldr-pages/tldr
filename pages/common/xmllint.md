# xmllint

> XML parser and linter.

- Return all nodes named "foo":

`xmllint --xpath "//{{foo}}" {{source_file.xml}}`

- Return as string the contents of first node named "foo":

`xmllint --xpath "string//{{foo}}" {{source_file.xml}}`

- Use other xpath (a syntax for navigating xml trees) expressions for more options in navigating xml tree:

`xmllint --xpath "{{xpath_expression}}" {{source_file.xml}}`

- Return human-readable (indented) xml from file:

`xmllint --format {{source_file.xml}}`

- Check that XML meets requirements of its built-in doctype. This is the part starting with `<!DOCTYPE...>`:

`xmllint --valid {{source_file.xml}}`

- Validate XML against DTD schema hosted online:

`xmllint --dtdvalid {{URL}} {{source_file.xml}}`
