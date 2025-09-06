# repren

> Multi-pattern string replacement and file renaming tool.
> More information: <https://github.com/jlevy/repren>.

- Do a dry-run renaming a directory of PNGs with a literal string replacement:

`repren {{[-n|--dry-run]}} --rename --literal --from '{{find_string}}' --to '{{replacement_string}}' {{*.png}}`

- Do a dry-run renaming a directory of JPEGs with a `regex`:

`repren --rename {{[-n|--dry-run]}} --from '{{regex}}' --to '{{replacement_string}}' {{*.jpg}} {{*.jpeg}}`

- Do a find-and-replace on the contents of a directory of CSV files:

`repren --from '{{([0-9]+) example_string}}' --to '{{replacement_string \1}}' {{*.csv}}`

- Do both a find-and-replace and a rename operation at the same time, using a pattern file:

`repren {{[-p|--patterns]}} {{path/to/patfile.ext}} --full {{*.txt}}`

- Do a case-insensitive rename:

`repren --rename {{[-i|--insensitive]}} {{[-p|--patterns]}} {{path/to/patfile.ext}} *`
