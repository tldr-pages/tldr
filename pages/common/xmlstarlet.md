# xmlstarlet

> A commandline XML/XSLT toolkit.
> More information: <https://xmlstar.sourceforge.net/docs.php>.

- Format an XML document and print to stdout:

`xmlstarlet format {{path/to/file.xml}}`

- XML document can also be piped from stdin:

`{{cat path/to/file.xml}} | xmlstarlet format`

- Print all nodes that match a given XPATH:

`xmlstarlet select --template --copy-of {{xpath}} {{file.xml}}`

- Insert an attribute to all matching nodes, and print to stdout (source file is unchanged):

`xmlstarlet edit --insert {{xpath}} --type attr --name {{attribute_name}} --value {{attribute_value}} {{file.xml}}`

- Rename some nodes, delete some nodes, and print to stdout (source file is unchanged):

`xmlstarlet edit --rename {{xpath_to_rename}} --value {{new_name}} --delete {{xpath_to_delete}} {{file.xml}}`

- Escape or unescape special XML characters in a given string:

`xmlstarlet [un]escape {{string}}`

- List a given directory as XML (omit argument to list current directory):

`xmlstarlet ls {{[path/to/directory]}}`
