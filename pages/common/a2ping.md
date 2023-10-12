# a2ping

> Convert images into EPS or PDF files.
> More information: <https://www.ctan.org/pkg/a2ping>.

- Convert an image to PDF. The output file name is optional:

`a2ping {{filename}} {{outputFilename.pdf}}`

- Compress the document using the specified method:

`a2ping --[no]compress {{none|zip|best|flate}} {{filename}}`

- Scan HiResBoundingBox. Defaults to yes:

`a2ping --[no]hires {{filename}}`

- Allow below or left_from baseline. Defaults to no:

`a2ping --[no]below {{filename}}`

- Pass extra arguments to gs:

`a2ping --gsextra {{arguments}} {{filename}}`

- Pass extra arguments to external prg:

`a2ping --extra {{arguments}} {{filename}}`

- Display the a2ping help:

`a2ping -h`
