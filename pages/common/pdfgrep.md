# pdfgrep

> Search text in PDF files.
> More information: <https://pdfgrep.org/doc.html>.

- Find lines that match pattern in a PDF:

`pdfgrep {{pattern}} {{file.pdf}}`

- Include file name and page number for each matched line:

`pdfgrep {{[-H|--with-filename]}} {{[-n|--page-number]}} {{pattern}} {{file.pdf}}`

- Do a case-insensitive search for lines that begin with "foo" and return the first 3 matches:

`pdfgrep {{[-m|--max-count]}} {{3}} {{[-i|--ignore-case]}} {{'^foo'}} {{file.pdf}}`

- Find pattern in files with a `.pdf` extension in the current directory recursively:

`pdfgrep {{[-r|--recursive]}} {{pattern}}`

- Find pattern on files that match a specific glob in the current directory recursively:

`pdfgrep {{[-r|--recursive]}} --include {{'*book.pdf'}} {{pattern}}`
