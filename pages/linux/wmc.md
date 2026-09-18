# wmc

> Compile Windows message files into resource data for Wine.
> More information: <https://manned.org/wmc>.

- Compile a message file (output defaults to `inputfile.rc`):

`wmc {{path/to/input.mc}}`

- Write the output to a specific file:

`wmc {{[-o|--output]}} {{path/to/output_file}} {{path/to/input.mc}}`

- Set the output format (default is `rc`; supports `rc`, `res`, and `pot`):

`wmc {{[-O|--output-format]}} {{format}} {{path/to/input.mc}}`

- Write a header file:

`wmc {{[-H]}} {{path/to/header_file.h}} {{path/to/input.mc}}`

- Assume the input is Unicode/UTF-8 and skip codepage conversions:

`wmc {{[-u]}} {{path/to/input.mc}}`
