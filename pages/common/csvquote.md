# csvquote

> Enables common unix utlities like cut, awk, wc, head to work correctly with csv data containing quoted delimiters and newlines
> More information: <https://github.com/dbro/csvquote>.

- Replace quoted special characters in normal csv file:

`csvquote {{data.csv}}`

- Replace quoted special characters in normal tsv file:

`csvquote -t {{data.csv}}`

- Restore quoted special characters from stdin:

`csvquote -u`

- Most common use case:

`csvquote {{data.csv}} | {{do_some_kind_of_processing}} | csvquote -u`
