# xml edit

> Edit an XML document.
> More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139594320>.

- Delete elements matching an XPATH from an XML document:

`xml {{[ed|edit]}} {{[-d|--delete]}} "{{XPATH1}}" {{path/to/input.xml|URI}}`

- Move an element node of an XML document from XPATH1 to XPATH2:

`xml {{[ed|edit]}} {{[-m|--move]}} "{{XPATH1}}" "{{XPATH2}}" {{path/to/input.xml|URI}}`

- Rename all attributes named "id" to "ID":

`xml {{[ed|edit]}} {{[-r|--rename]}} "{{//*/@id}}" -v "{{ID}}" {{path/to/input.xml|URI}}`

- Rename sub-elements of the element "table" that are named "rec" to "record":

`xml {{[ed|edit]}} {{[-r|--rename]}} "{{/xml/table/rec}}" -v "{{record}}" {{path/to/input.xml|URI}}`

- Update the XML table record with "id=3" to the value "id=5":

`xml {{[ed|edit]}} {{[-u|--update]}} "{{xml/table/rec[@id=3]/@id}}" {{[-v|--value]}} {{5}} {{path/to/input.xml|URI}}`

- Display help:

`xml {{[ed|edit]}} {{[-h|--help]}}`
