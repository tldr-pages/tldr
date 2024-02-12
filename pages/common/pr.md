# pr

> Paginate or columnate files for printing.
> More information: <https://www.gnu.org/software/coreutils/pr>.

- Print multiple files with a default header and footer:

`pr {{path/to/file1 path/to/file2 ...}}`

- Print with a custom centered header:

`pr -h "{{header}}" {{path/to/file1 path/to/file2 ...}}`

- Print with numbered lines and a custom date format:

`pr -n -D "{{format}}" {{path/to/file1 path/to/file2 ...}}`

- Print all files together, one in each column, without a header or footer:

`pr -m -T {{path/to/file1 path/to/file2 ...}}`

- Print, beginning at page 2 up to page 5, with a given page length (including header and footer):

`pr +{{2}}:{{5}} -l {{page_length}} {{path/to/file1 path/to/file2 ...}}`

- Print with an offset for each line and a truncating custom page width:

`pr -o {{offset}} -W {{width}} {{path/to/file1 path/to/file2 ...}}`
