# wdf

> Wiimms WDF Tool for packing, unpacking, comparing, and dumping WDF, WIA, CISO, and GCZ images.
> More information: <https://wit.wiimm.de/wdf/>.

- Pack files into a WDF image:

`wdf +PACK {{path/to/source}} --dest {{path/to/output.wdf}}`

- Unpack a WDF, WIA, or CISO image:

`wdf +UNPACK {{path/to/input.wdf}} --dest {{path/to/output_directory}}`

- Compare two images:

`wdf +DIFF {{path/to/image1.wdf}} {{path/to/image2.wdf}}`

- Dump the data structure of an image:

`wdf +DUMP {{path/to/image.wdf}}`

- Concatenate files and write the result to standard output:

`wdf +CAT {{path/to/input.wdf}} > {{path/to/output.iso}}`

- Display help:

`wdf +HELP`

- Display version information:

`wdf +VERSION`
