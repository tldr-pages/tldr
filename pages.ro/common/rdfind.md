# rdfind

> Găsiți fișiere cu conținut duplicat și scăpați de ele.
> Mai multe informaţii: <https://rdfind.pauldreik.se>

- Identificați toate duplicatele dintr-un anumit director și ieșiți un rezumat:

`rdfind -dryrun true {{path/to/directory}}`

- Înlocuiți toate duplicatele cu hardlink-uri:

`rdfind -makehardlinks true {{path/to/directory}}`

- Înlocuiți toate duplicatele cu simlinkuri/link-uri soft:

`rdfind -makesymlinks true {{path/to/directory}}`

- Ștergeți toate duplicatele și nu ignorați fișierele goale:

`rdfind -deleteduplicates true -ignoreempty false {{path/to/directory}}`
