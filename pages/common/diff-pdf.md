# diff-pdf

> Compare two PDFs.
> More information: <https://github.com/vslavik/diff-pdf>.

- Compare PDFs, indicating changes using return codes (`0` = no difference, `1` = PDFs differ):

`diff-pdf {{path/to/a.pdf}} {{path/to/b.pdf}}`

- Compare PDFs, outputting a PDF with visually highlighted differences:

`diff-pdf --output-diff={{path/to/diff.pdf}} {{path/to/a.pdf}} {{path/to/b.pdf}}`

- Compare PDFs, viewing differences in a simple GUI:

`diff-pdf --view {{path/to/a.pdf}} {{path/to/b.pdf}}`
