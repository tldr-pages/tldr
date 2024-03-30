# ppmtoarbtxt

> Convert a PPM image to an arbitrary text format according to a template.
> More information: <https://netpbm.sourceforge.net/doc/ppmtoarbtxt.html>.

- Convert a PPM image to text as specified by the given template:

`ppmtoarbtxt {{path/to/template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- Convert a PPM image to text as specified by the given template, prepend the contents of the specified head template:

`ppmtoarbtxt {{path/to/template}} -hd {{path/to/head_template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- Convert a PPM image to text as specified by the given template, append the contents of the specified tail template:

`ppmtoarbtxt {{path/to/template}} -hd {{path/to/tail_template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- Display version:

`ppmtoarbtxt -version`
