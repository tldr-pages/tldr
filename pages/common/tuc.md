# tuc

> Cut text (or bytes) where a delimiter matches, then keep the desired parts.
> A more user-friendly and powerful version of `cut` with sensible defaults.
> More information: <https://github.com/riquito/tuc#help>.

- Cut and rearrange fields:

`echo "foo bar baz" | tuc {{[-d|--delimiter]}} '{{ }}' {{[-f|--fields]}} {{3,2,1}}`

- Replace the delimiter `space` with an arrow:

`echo "foo bar baz" | tuc {{[-d|--delimiter]}} ' ' {{[-r|--replace-delimiter]}} ' ➡ '`

- Keep a range of fields:

`echo "foo bar    baz" | tuc {{[-d|--delimiter]}} ' ' {{[-f|--fields]}} {{2:}}`

- Cut using `regex`:

`echo "a,b, c" | tuc {{[-e|--regex]}} '{{[, ]+}}' {{[-f|--fields]}} {{1,3}}`

- Emit JSON output:

`echo "foo bar baz" | tuc {{[-d|--delimiter]}} '{{ }}' --json`
