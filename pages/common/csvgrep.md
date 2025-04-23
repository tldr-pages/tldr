# csvgrep

> Filter CSV rows with string and pattern matching.
> Included in csvkit.
> More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- Find rows that have a certain string in column 1:

`csvgrep {{[-c|--columns]}} {{1}} {{[-m|--match]}} {{string_to_match}} {{data.csv}}`

- Find rows in which columns 3 or 4 match a certain regular expression:

`csvgrep {{[-c|--columns]}} {{3,4}} {{[-r|--regex]}} {{regular_expression}} {{data.csv}}`

- Find rows in which the "name" column does NOT include the string "John Doe":

`csvgrep {{[-i|--invert-match]}} {{[-c|--columns]}} {{name}} {{[-m|--match]}} "{{John Doe}}" {{data.csv}}`
