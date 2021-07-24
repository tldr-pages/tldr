# ffe

> Extract fields from a flat database file and write to another format.
> `ffe` needs a text config file to interpret the input and format the output.
> More information: <http://ff-extractor.sourceforge.net/ffe.html>.

- Display all input data using the specified data configuration:

`ffe -c {{path/to/config}} {{path/to/input}}`

- Convert an input file to an output file in a new format:

`ffe -o {{path/to/output}} -c {{path/to/config}} {{path/to/input}}`

- Interpret input with a selected structure and write with a selected print format:

`ffe -s {{structure}} -p {{format}} -c {{path/to/config}} {{path/to/input}}`

- Write only the selected fields:

`ffe -f "{{FirstName,LastNAme,Age}}" -c {{path/to/config}} {{path/to/input}}`

- Write only the records that match an expression:

`ffe -e "{{LastName=Smith}}" -c {{path/to/config}} {{path/to/input}}`

- Display help:

`ffe --help`
