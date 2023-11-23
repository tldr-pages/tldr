# xwdtopnm

> Convert an X11 or X10 window dump file to PNM.
> More information: <https://netpbm.sourceforge.net/doc/xwdtopnm.html>.

- Convert a XWD image file to PBM:

`xwdtopnm {{path/to/input_file.xwd}} > {{path/to/output_file.pnm}}`

- Display information about the conversion process:

`xwdtopnm -verbose {{path/to/input_file.xwd}} > {{path/to/output_file.pnm}}`

- Display the contents of the X11 header of the input file:

`xwdtopnm -headerdump {{path/to/input_file.xwd}} > {{path/to/output_file.pnm}}`
