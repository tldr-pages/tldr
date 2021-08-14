# xml

> XMLStarlet toolkit: Query / Edit / Check / Transform XML documents.
> Subcommands: `canonic`, `edit`, `elements`, `escape`, `format`, `list`, `pyx`, `p2x`, `select`, `transform`, `unescape`, or `validate`.
> More information: <https://http://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Execute a subcommand with input from a file and using standard output:

`xml {{subcommand}} {{options}} {{xml_file_or_uri}}`

- Execute a subcommand using standard input and standard output:

`xml {{subcommand}} {{options}}`

- Execute a subcommand with input from a file and output to a file:

`xml {{subcommand}} {{options}} {{xml_file_or_uri}} >{{path/to/output}}`

- Display help for a subcommand:

`xml {{subcommand}} --help`

- Display general help:

`xml --help`

- Display version:

`xml --version`
