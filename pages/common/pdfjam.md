# pdfjam

> Shell frontend for the LaTeX pdfpages package for mingling PDFs.
> More information: <https://github.com/rrthomas/pdfjam>.

- Merge two (or more) PDFs:

`pdfjam {{file1}} {{file2}} --outfile {{output_file}}`

- Merge the first page of each file together:

`pdfjam {{files...}} 1 --outfile {{output_file}}`

- Merge subranges from two PDFs:

`pdfjam {{file1 3-5,1}} {{file2 4-6}} --outfile {{output_file}}`

- Sign an A4 page (adjust delta to height for other formats) with a scanned signature by overlaying them:

`pdfjam {{file}} {{signature}} --outfile signed.pdf --nup "1x2" --fitpaper true --delta "0 -842pt"`

- Arrange the pages from the input file into a fancy 2x2 grid:

`pdfjam --nup 2x2 {{file}} --suffix 4up --preamble '\usepackage{fancyhdr} \pagestyle{fancy}'`

- Reverse the order of pages within each given file and concatenate them:

`pdfjam {{files...}} last-1 --suffix reversed`
