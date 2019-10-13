# pr

> Paginate or columnate files for printing.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/pr-invocation.html>.

- Print multiple files with a default header and footer:

`pr {{file1 file2 file3}}`

- Print all files in parallel, one in each column without a header or footer:

`pr -m -t {{file1 file2 file3}}`

- Print all files beginning at 2 up to 5 with a given page length (including header and footer):

`pr +{{2}}:{{5}} -l {{page_length}} {{file1 file2 file3}}`

- Print all files with an offset each line and a truncating custom page width:

`pr -o {{offset}} -W {{width}} {{file1 file2 file3}}`

- Print files with numbered lines, a custom centered header and date format:

`pr -n -h "{{header}}" -D "{{%Y.%m.%d - %H:%M:%S}}" {{file1 file2 file3}}`
