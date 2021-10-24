# pr

> Paginate or columnate files for printing.
> More information: <https://www.gnu.org/software/coreutils/pr>.

- Print multiple files with a default header and footer:

`pr {{file1}} {{file2}} {{file3}}`

- Print with a custom centered header:

`pr -h "{{header}}" {{file1}} {{file2}} {{file3}}`

- Print with numbered lines and a custom date format:

`pr -n -D "{{format}}" {{file1}} {{file2}} {{file3}}`

- Print all files together, one in each column, without a header or footer:

`pr -m -T {{file1}} {{file2}} {{file3}}`

- Print, beginning at page 2 up to page 5, with a given page length (including header and footer):

`pr +{{2}}:{{5}} -l {{page_length}} {{file1}} {{file2}} {{file3}}`

- Print with an offset for each line and a truncating custom page width:

`pr -o {{offset}} -W {{width}} {{file1}} {{file2}} {{file3}}`
