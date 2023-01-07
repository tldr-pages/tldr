# tsv-filter

> Filter lines of a TSV file by running tests against individual fields.
> More information: <https://github.com/eBay/tsv-utils#tsv-filter>.

- Print the lines where a specific column is numerically equal to a given number:

`tsv-filter -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`

- Print the lines where a specific column is [eq]ual/[n]on [e]qual/[l]ess [t]han/[l]ess than or [e]qual/[g]reater [t]han/[g]reater than or [e]qual to a given number:

`tsv-filter --{{eq|ne|lt|le|gt|ge}} {{column_number}}:{{number}} {{path/to/tsv_file}}`

- Print the lines where a specific column is [eq]ual/[n]ot [e]qual/part of/not part of a given string:

`tsv-filter --str-{{eq|ne|in-fld|not-in-fld}} {{column_number}}:{{string}} {{path/to/tsv_file}}`

- Filter for non-empty fields:

`tsv-filter --not-empty {{column_number}} {{path/to/tsv_file}}`

- Print the lines where a specific column is empty:

`tsv-filter --invert --not-empty {{column_number}} {{path/to/tsv_file}}`

- Print the lines that satisfy two conditions:

`tsv-filter --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- Print the lines that match at least one condition:

`tsv-filter --or --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- Count matching lines, interpreting first line as a [H]eader:

`tsv-filter --count -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`
