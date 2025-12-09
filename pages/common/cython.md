# cython

> A compiler that converts .pyx files into C or C++ source files.
> More information: <https://docs.cython.org/en/latest/>.

- Compile into C code:

`cython {{path/to/file}}`

- Compile into C++ code:

`cython --cplus {{path/to/file}}`

- Specify an output file:

`cython {{[-o|--output-file]}} {{path/to/output_file}} {{path/to/file}}`

- Display version:

`cython {{[-V|--version]}}`
