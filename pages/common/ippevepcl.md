# ippevepcl

> Print to B&W HP PCL laser printers.
> Supports HP PCL, PWG Raster and Apple Raster files.
> See also: `ippevepcl`, `ippeveprinter`.
> More information: <https://openprinting.github.io/cups/doc/man-ippevepcl.html>.

- Print a file to `stdout` (status and progress messages are sent to `stderr`):

`ippeveps {{path/to/file}}`

- Print a file from `stdin` to `stdout`:

`{{wget -O - https://examplewebsite.com/file}} | ippeveps`
