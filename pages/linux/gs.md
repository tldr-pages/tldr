# gs

> GhostScript is a PDF and PostScript interpreter.

- To view a file:

`gs -dQUIET -dBATCH {{file.pdf}}`

- Reduce PDF file size to 150 dpi images for reading on a ebook device:

`gs -dNOPAUSE -dQUIET -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile={{output.pdf}} {{input.pdf}}`

- Convert PDF file to an image:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=jpeg -r150 -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dFirstPage=1 -dLastPage=3 -sOutputFile={{output_%d.jpg}} {{input.pdf}}`

- Extract pages from a PDF file:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dFirstPage=1 -dLastPage=3 -sOutputFile={{output.pdf}} {{input.pdf}}`

- Merge PDF files:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input1.pdf}} {{input2.pdf}}`

- Convert from PostScript file to PDF file:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input.ps}}`

<!---
Remove this before merging.
I dont know how to proceed with explaining the used options, there is too many of them to do step-by-step through gradually adding examples and meet the 8 example limit.

The ones that I used are:
-dNOPAUSE (no pause after page)
-dBATCH (exit after last file)
-dQUIET (suppresses normal startup messages)
-dPDFSETTINGS=/ebook (renders lower quality, 150 dpi images)
-sDEVICE=pdfwrite (outputs PDF)
-r150 (resolution 150 dpi)
-dTextAlphaBits=4 (option that controls the use of subsample antialiasing for text, 4 for optimum output, but smaller values for faster rendering)
-dGraphicsAlphaBits=4 (option that controls the use of subsample antialiasing for graphics, 4 for optimum output, but smaller values for faster rendering)

Common possibilities:
-dPDFSETTINGS=/screen (screen-view-only quality, 72 dpi images)
-dPDFSETTINGS=/printer (high quality, 300 dpi images)
-dPDFSETTINGS=/prepress (high quality, color preserving, 300 dpi images)

-sDEVICE=ps2write
-sDEVICE=png16m  (24-bit RGB color)
-sDEVICE=pnggray  (grayscale)
-sDEVICE=pngmono  (black-and-white)
-sDEVICE=pngalpha (32-bit RGBA color)
-sDEVICE=jpeg   (color JPEG)
-sDEVICE=jpeggray  (grayscale JPEG)
-sDEVICE=epswrite  (encapsulated postscript)
-sDEVICE=txtwrite  (text output, UTF-8)
-->
