# sed

> GNU stream editor for filtering and transforming text.
> See also: `awk`, `ed`.
> More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- [s]ubstitute all occurrences of "apple" with "mango" on all lines, print to `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Replace "apple" with "mango" in-place in a file (overwriting original file):

`sed {{[-i|--in-place]}} 's/apple/mango/g' {{path/to/file}}`

- Run multiple substitutions in one command:

`{{command}} | sed -e '{{s/apple/mango/g}}' -e '{{s/orange/lime/g}}'`

- Use a custom delimiter (useful when the pattern contains slashes):

`{{command}} | sed '{{s#////#____#g}}'`

- [d]elete lines 1 to 5 of a file and back up the original file with a `.orig` extension:

`sed {{[-i|--in-place=]}}{{.orig}} '1,5d' {{path/to/file}}`

- [p]rint only the first line to `stdout`:

`{{command}} | sed {{[-n|--quiet]}} '1p'`

- [i]nsert a new line at the beginning of a file, overwriting the original file:

`sed {{[-i|--in-place]}} '1i\your new line text\' {{path/to/file}}`

- Delete blank lines (with or without spaces/tabs) from a file, overwriting the original file:

`sed {{[-i|--in-place]}} '/^[[:space:]]*$/d' {{path/to/file}}`
