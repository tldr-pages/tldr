# tsv-filter

> Filter lines of a TSV file by running tests against individual fields.
> More information: <https://github.com/eBay/tsv-utils#tsv-filter>.

- Output all lines where column with field_name is numerically equal to value:

`tsv-filter -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`

- Filter using numeric equality/non-equality/less-than/less-or-equal/greater-than/greater-or-equal:

`tsv-filter --{{eq|ne|lt|le|gt|ge}} {{column_number}}:{{number}} {{path/to/tsv_file}}`

- Filter on string (in-)equality, partial strings, case insensitive:

`tsv-filter --{{str-eq|str-ne|str-in-fld|str-not-in-fld}} {{column_number}}:{{string}} {{path/to/tsv_file}}`

- Filter for non-empty fields:

`tsv-filter --not-empty {{column_number}} {{path/to/tsv_file}}`

- Show fields that are empty in column_number:

`tsv-filter --invert --not-empty {{column_number}} {{path/to/tsv_file}}`

- Filter lines that satisfy two conditions:

`tsv-filter --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- Filter lines that match at least one condition:

`tsv-filter --or --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- Count matching lines, interpreting first line as [H]eader:

`tsv-filter --count -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`
