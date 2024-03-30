# pngtopam

> Convert a PNG image to a Netpbm image.
> See also: `pamtopng`.
> More information: <https://netpbm.sourceforge.net/doc/pngtopam.html>.

- Convert the specified PNG image to a Netpbm image:

`pngtopam {{path/to/image.png}} > {{path/to/output.pam}}`

- Create an output image that includes both the main image and transparency mask of the input image:

`pngtopam -alphapam {{path/to/image.png}} > {{path/to/output.pam}}`

- Replace transparent pixels by the specified color:

`pngtopam -mix -background {{color}} {{path/to/image.png}} > {{path/to/output.pam}}`

- Write tEXt chunks found in the input image to the specified text file:

`pngtopam -text {{path/to/file.txt}} {{path/to/image.png}} > {{path/to/output.pam}}`
