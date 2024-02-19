# pbmtext

> Render text as a PBM image.
> See also: `pbmtextps`.
> More information: <https://netpbm.sourceforge.net/doc/pbmtext.html>.

- Render a single line of text as a PBM image:

`pbmtext "{{Hello World!}}" > {{path/to/output.pbm}}`

- Render multiple lines of text as a PBM image:

`echo "{{Hello\nWorld!}}" | pbmtext > {{path/to/output.pbm}}`

- Render text using a custom font supplied as a PBM file:

`pbmtext -font {{path/to/font.pbm}} "{{Hello World!}}" > {{path/to/output.pbm}}`

- Specify the number of pixels between characters and lines:

`echo "{{Hello\nWorld!}}" | pbmtext -space {{3}} -lspace {{10}} > {{path/to/output.pbm}}`
