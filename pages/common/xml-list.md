# xml list

> List a directory's contents (like `ls`) in XML format.
> More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139535968>.

- Write the current directory's listing to an XML document:

`xml {{[ls|list]}} > {{path/to/dir_list.xml}}`

- Write the specified directory's listing to an XML document:

`xml {{[ls|list]}} {{path/to/directory}} > {{path/to/dir_list.xml}}`

- Display help:

`xml {{[ls|list]}} --help`
