# xsv

> A fast CSV command line toolkit written in Rust.

- Inspect the headers of a file:

`xsv headers {{worldcities.csv}}`

- Count the number of entries:

`xsv count {{worldcities.csv}}`

- Get an overview of the shape of entries:

`xsv stats {{worldcities.csv}} | xsv table`

- Select a few columns:

`xsv select {{Country,AccentCity}} {{worldcities.csv}}`

- Show 10 random sample of entries:

`xsv sample {{10}} {{worldcities.csv}}`

- Join a column from one file to another:

`xsv join --no-case {{Country}} {{worldcities.csv}} {{Abbrev}} {{countrynames.csv}} | xsv table`
