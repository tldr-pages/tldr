# xsv

> A fast CSV command line toolkit written in Rust.

- Inspect the headers of a file:

`xsv headers {{path/to/worldcities.csv}}`

- Count the number of entries:

`xsv count {{path/to/worldcities.csv}}`

- Get an overview of the shape of entries:

`xsv stats {{path/to/worldcities.csv}} | xsv table`

- Select a few columns:

`xsv select {{Country,AccentCity}} {{path/to/worldcities.csv}}`

- Show 10 random entries:

`xsv sample {{10}} {{path/to/worldcities.csv}}`

- Join a column from one file to another:

`xsv join --no-case {{Country}} {{path/to/worldcities.csv}} {{Abbrev}} {{path/to/countrynames.csv}} | xsv table`
