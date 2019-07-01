# xsv

> A fast CSV command line toolkit written in Rust.
> More information: <https://github.com/BurntSushi/xsv>.

- Inspect the headers of a file:

`xsv headers {{path/to/file.csv}}`

- Count the number of entries:

`xsv count {{path/to/file.csv}}`

- Get an overview of the shape of entries:

`xsv stats {{path/to/file.csv}} | xsv table`

- Select a few columns:

`xsv select {{column_a,column_b}} {{path/to/file.csv}}`

- Show 10 random entries:

`xsv sample {{10}} {{path/to/file.csv}}`

- Join a column from one file to another:

`xsv join --no-case {{column_a}} {{path/to/file/a.csv}} {{column_b}} {{path/to/file/b.csv}} | xsv table`
