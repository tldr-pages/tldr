# pdfgrep

> Search text in PDF files.

- Find lines that match pattern in a PDF:

`pdfgrep {{pattern}} {{file.pdf}}`

- Include file name and page number for each matched line:

`pdfgrep --with-filename --page-number {{pattern}} {{file.pdf}}`

- Find the first 3 lines that begin with foo case insensitive:

`pdfgrep --max-count {{3}} --ignore-case {{'^foo'}} {{file.pdf}}`

- Find pattern in pdf files under the current directory recusively:

`pdfgrep --recursive --include {{'*.pdf'}} {{pattern}}`
