# winicontopam

> Convert a Windows ICO file to a PAM file.
> More information: <https://netpbm.sourceforge.net/doc/winicontopam.html>.

- Read an ICO file and convert the best quality image contained therein to the PAM format:

`winicontopam {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- Convert all images in the input file to PAM:

`winicontopam -allimages {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- Convert the n'th image in the input file to PAM:

`winicontopam -image {{n}} {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- If the image(s) to be extracted contain graded transparency data and an AND mask, write the AND mask into the fifth channel of the output PAM file:

`winicontopam -andmasks {{path/to/input_file.ico}} > {{path/to/output.pam}}`
