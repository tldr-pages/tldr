# cython

> A compiler that converts .pyx files into C or C++ source files.
> More information: <https://docs.cython.org/en/latest/>.

- Compile into C code:

`cython {{path_to_file}}`

- Compile into C++ code:

`cython --cplus {{path_to_file}}`

- Specify an output file:

`cython {{[-o|--output-file]}} {{path_to_output_file}} {{path_to_file}}`

- Show the version:

`cython {{[-V|--version]}}`
