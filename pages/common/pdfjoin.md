# pdfjoin

> PDF merging utility based on pdfjam.
> More information: <https://github.com/rrthomas/pdfjam-extras>.

- Merge two PDFs into one with the default suffix "joined":

`pdfjoin {{file1}} {{file2}}`

- Merge the first page of each given file together:

`pdfjoin {{files...}} 1 --outfile {{output_file}}`

- Save pages 3 to 5 followed by page 1 to a new PDF:

`pdfjoin {{file 3-5,1}} --outfile {{output_file}}`

- Merge page subranges from two PDFs:

`pdfjoin {{file1 3-5,1}} {{file2 4-6}} --outfile {{output_file}}`
