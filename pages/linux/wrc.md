# wrc

> Compile Windows resource scripts into binary resource files for Wine.
> More information: <https://manned.org/wrc>.

- Compile a resource script (output defaults to `inputfile.res`):

`wrc {{path/to/input.rc}}`

- Write the output to a specific file:

`wrc {{[-o|--output]}} {{path/to/output_file}} {{path/to/input.rc}}`

- Define a preprocessor macro:

`wrc {{[-D|--define]}} {{id[=val]}} {{path/to/input.rc}}`

- Preprocess only, writing the result to standard output:

`wrc {{[-E]}} {{path/to/input.rc}}`

- Display help:

`wrc {{[-h|--help]}}`
