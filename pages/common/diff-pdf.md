# diff-pdf

> Tool for visually comparing two PDFs.
> More information: <https://github.com/vslavik/diff-pdf>.

- Compare PDFs, (return code 0 = no differences, return code 1 = PDFs differ):

`diff-pdf a.pdf b.pdf`

- Compare PDFs, output PDF with visually highlighted differences:

`diff-pdf --output-diff=diff.pdf a.pdf b.pdf`

- Compare PDFs, view differences in a simple GUI:

`diff-pdf --view a.pdf b.pdf`
