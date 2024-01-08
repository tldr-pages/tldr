# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/man/sed.1posix>.

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Execute a specific script [f]ile and print the result to `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Print just a first line to `stdout`:

`{{command}} | sed -n '1p'`
