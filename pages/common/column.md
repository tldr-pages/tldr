# column

> Format standard or file input into multiple columns, rows are filled before columns.

- Output is formatted for a display columns wide:

`printf "header1 header2\nbar foo\n" | column -c 10`

- Specify a set of characters to be used to delimit columns for the -t option, default is whitespace:

`printf "header1,header2\nbar,foo\n" | column -s,`

- Determine the number of columns the input contains and create a table:

`printf "header1 header2\nbar foo\n" | column -t`

- Fill columns before filling rows:

`printf "header1\nbar\nfoobar\n" | column -c 20 -x`
