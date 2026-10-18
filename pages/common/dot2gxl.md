# dot2gxl

> Convert between graphs represented in GXL and in the DOT language.
> More information: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- Convert a DOT graph to GXL:

`dot2gxl {{path/to/input_file.dot}} -o {{path/to/output_file.gxl}}`

- Convert DOT to GXL based on .dot input extension:

`dot2gxl {{path/to/input_file.dot}} > {{path/to/output_file.gxl}}`

- Convert GXL to DOT based on .gxl input extension:

`dot2gxl {{path/to/input_file.gxl}} > {{path/to/output_file.dot}}`
