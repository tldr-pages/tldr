# a2ping

> Convert images into EPS or PDF files.
> More information: <https://manned.org/a2ping>.

- Convert an image to PDF (Note: Specifying an output filename is optional):

`a2ping {{path/to/image.ext}} {{path/to/output.pdf}}`

- Compress the document using the specified method:

`a2ping --nocompress {{none|zip|best|flate}} {{path/to/file}}`

- Scan HiResBoundingBox if present (Note: It Defaults to yes):

`a2ping --nohires {{path/to/file}}`

- Allow page content below and left of the origin (Note: It defaults to no):

`a2ping --below {{path/to/file}}`

- Pass extra arguments to `gs``:

`a2ping --gsextra {{arguments}} {{path/to/file}}`

- Pass extra arguments to external program (i.e pdftops):

`a2ping --extra {{arguments}} {{path/to/file}}`

- Display help:

`a2ping -h`
