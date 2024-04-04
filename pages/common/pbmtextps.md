# pbmtextps

> Render text as a PBM image using PostScript.
> See also: `pbmtext`.
> More information: <https://netpbm.sourceforge.net/doc/pbmtextps.html>.

- Render a single line of text as a PBM image:

`pbmtextps "{{Hello World!}}" > {{path/to/output.pbm}}`

- Specify the font and font size:

`pbmtextps -font {{Times-Roman}} -fontsize {{30}}  "{{Hello World!}}" > {{path/to/output.pbm}}`

- Specify the desired left and top margins:

`pbmtextps -leftmargin {{70}} -topmargin {{162}}  "{{Hello World!}}" > {{path/to/output.pbm}}`

- Do not output the rendered text as a PBM image, but a PostScript program that would create this image:

`pbmtextps -dump-ps "{{Hello World!}}" > {{path/to/output.ps}}`
