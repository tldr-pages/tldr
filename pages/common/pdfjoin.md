# pdfjoin

> PDF merging utility.

- Merge two PDFs:

`pdfjoin {{file1}} {{file2}} --outfile {{output_file}}`

- Save pages 3 to 5 followed by page 1 to a new PDF:

`pdfjoin {{file 3-5,1}} --outfile {{output_file}}`

- Merge subranges from two PDFs:

`pdfjoin {{file1 3-5,1}} {{file2 4-6}} --outfile {{output_file}}`
