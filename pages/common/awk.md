# awk

> A versatile programming language for working on files.
> See also: `sed`, `ed`.
> More information: <https://github.com/onetrueawk/awk>.

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:

`{{command}} | awk '{ print gensub("apple", "mango", "g") }'`

- Execute a specific script [f]ile and print the result to `stdout`:

`{{command}} | awk -f {{path/to/script.awk}}`

- Print first fields of all input lines delimited by a specific delimiter (basic regex) to `stdout`:

`{{command}} | awk -F ',' '{ print $1 }'`

- Print first 10 fields of all input lines delimited by a single space (basic regex) to `stdout`:

`{{command}} | awk '{ for (i = 1; i <= 10; i++) print $i }'`
