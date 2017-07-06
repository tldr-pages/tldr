# xmllint

> XML parser.
> Also useful for detecting errors in XML code.

- Return all nodes named {{foo}}:

`xmllint --xpath "//{{foo}}" {{source_file.xml}}`

- Return as string the contents of first node named {{foo}}:

`xmllint --xpath "string//{{foo}}" {{source_file.xml}}`

- Use other other xpath expressions for more options in navigating xml tree. NOTE: xpath is a syntax for navigating XML trees too extensive to be covered here:

`xmllint --xpath "{{xpath_expression}}" {{source_file.xml}}`

- Return human-readable (indented) xml from file:

`xmllint --format {{source_file.xml}}`

- Return human-readable xml from terminal:

`echo "{{some_xml}}" | xmllint --format -`

- Check that XML meets requirements of its built-in doctype. This is the part starting with <!DOCTYPE...>:

`xmllint --valid {{source_file.xml}}`

- Validate XML against DTD schema hosted online:

`xmllint --dtdvalid {{URL}} {{source_file.xml}}`
