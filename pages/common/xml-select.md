# xml select

> Select from XML documents using XPATHs.
> Tip: use `xml elements` to display the XPATHs of an XML document.
> More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139652416>.

- Select all elements matching "XPATH1" and print the value of their sub-element "XPATH2":

`xml {{[sel|select]}} {{[-t|--template]}} {{[-m|--match]}} "{{XPATH1}}" {{[-v|--value-of]}} "{{XPATH2}}" {{path/to/input.xml|uri}}`

- Match "XPATH1" and print the value of "XPATH2" as text with new-lines:

`xml {{[sel|select]}} {{[-T|--text]}} {{[-t|--template]}} {{[-m|--match]}} "{{XPATH1}}" {{[-v|--value-of]}} "{{XPATH2}}" {{[-n|--nl]}} {{path/to/input.xml|uri}}`

- Count the elements of "XPATH1":

`xml {{[sel|select]}} {{[-t|--template]}} {{[-v|--value-of]}} "count({{XPATH1}})" {{path/to/input.xml|uri}}`

- Count all nodes in one or more XML documents:

`xml {{[sel|select]}} {{[-T|--text]}} {{[-t|--template]}} {{[-f|--inp-name]}} {{[-o|--output]}} " " {{[-v|--value-of]}} "count(node())" {{[-n|--nl]}} {{path/to/input1.xml|uri}} {{path/to/input2.xml|uri}}`

- Display help:

`xml {{[sel|select]}} --help`
