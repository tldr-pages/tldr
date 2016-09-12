# column

> Format standard or file input into multiple columns, rows are filled before columns.

- Output is formatted for a 10 columns wide display:

`printf "header1 header2\nbar foo\n" | column -c {{10}}`

- Specify characters to use to delimit columns for the -t option (i.e. "," for csv), default is whitespace:

`printf "header1,header2\nbar,foo\n" | column -s{{,}}`

- Determine the number of columns and auto-align the output in a tabular format:

`printf "header1 header2\nbar foo\n" | column -t`

- Fill columns before filling rows:

`printf "header1\nbar\nfoobar\n" | column -c {{20}} -x`
