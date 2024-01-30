# xml edit

> Edit an XML document.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Delete elements matching an XPATH from an XML document:

`xml edit --delete "{{XPATH1}}" {{path/to/input.xml|URI}}`

- Move an element node of an XML document from XPATH1 to XPATH2:

`xml edit --move "{{XPATH1}}" "{{XPATH2}}" {{path/to/input.xml|URI}}`

- Rename all attributes named "id" to "ID":

`xml edit --rename "{{//*/@id}}" -v "{{ID}}" {{path/to/input.xml|URI}}`

- Rename sub-elements of the element "table" that are named "rec" to "record":

`xml edit --rename "{{/xml/table/rec}}" -v "{{record}}" {{path/to/input.xml|URI}}`

- Update the XML table record with "id=3" to the value "id=5":

`xml edit --update "{{xml/table/rec[@id=3]/@id}}" -v {{5}} {{path/to/input.xml|URI}}`

- Display help:

`xml edit --help`
