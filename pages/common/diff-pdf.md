# diff-pdf

> Tool for visually comparing two PDFs.
> More information: <https://github.com/vslavik/diff-pdf>.

- Outputs a return code, 0 if there are no differences and 1 if the two PDFS differ:

`diff-pdf a.pdf b.pdf`

- Outputs PDF file with visually highlighted differences:

`diff-pdf --output-diff=diff.pdf a.pdf b.pdf`

- Compares the two PDFs visually in a simple GUI:

`diff-pdf --view a.pdf b.pdf`
