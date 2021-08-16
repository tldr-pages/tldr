# xml

> XMLStarlet Toolkit: Query, edit, check, convert and transform XML documents.
> Subcommands: `canonic`, `edit`, `elements`, `escape`, `unescape`, `format`, `list`, `pyx`, `depyx`, `select`, `transform`, or `validate`.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Execute a subcommand with input from a file or URI and using standard output:

`xml {{subcommand}} {{options}} {{path/to/input.xml|URI}}`

- Execute a subcommand using the standard input and standard output:

`xml {{subcommand}} {{options}}`

- Execute a subcommand with input from a file or URI and output to a file:

`xml {{subcommand}} {{options}} {{path/to/input.xml|URI}} >{{path/to/output}}`

- Display help for a subcommand:

`xml {{subcommand}} --help`

- Display general help:

`xml --help`

- Display version:

`xml --version`
