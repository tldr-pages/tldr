# xml select

> Select from XML documents using XPATHs.
> Tip: use `xml elements` to display the XPATHs of an XML document.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Select all elements matching "XPATH1" and print the value of their sub-element "XPATH2":

`xml select --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" {{path/to/input.xml|URI}}`

- Match  "XPATH1" and print the value of "XPATH2" as text with new-lines:

`xml select --text --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" --nl {{path/to/input.xml|URI}}`

- Count the elements of "XPATH1":

`xml select --template --value-of "count({{XPATH1}})" {{path/to/input.xml|URI}}`

- Count all nodes in one or more XML documents:

`xml select --text --template --inp-name --output " " --value-of "count(node())" --nl {{path/to/input1.xml|URI}} {{path/to/input2.xml|URI}}`

- Display help for the `select` subcommand:

`xml select --help`
