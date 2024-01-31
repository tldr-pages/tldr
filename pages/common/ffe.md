# ffe

> Extract fields from a flat database file and write to another format.
> A configuration file is required to interpret the input and format the output.
> More information: <http://ff-extractor.sourceforge.net/ffe.html>.

- Display all input data using the specified data configuration:

`ffe --configuration={{path/to/config.ffe}} {{path/to/input}}`

- Convert an input file to an output file in a new format:

`ffe --output={{path/to/output}} -c {{path/to/config.ffe}} {{path/to/input}}`

- Select input structure and print format from definitions in `~/.fferc` configuration file:

`ffe --structure={{structure}} --print={{format}} {{path/to/input}}`

- Write only the selected fields:

`ffe --field-list="{{FirstName,LastName,Age}}" -c {{path/to/config.ffe}} {{path/to/input}}`

- Write only the records that match an expression:

`ffe -e "{{LastName=Smith}}" -c {{path/to/config.ffe}} {{path/to/input}}`

- Display help:

`ffe --help`
