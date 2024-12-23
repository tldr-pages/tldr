# tuc

> Cut text (or bytes) where a delimiter matches, then keep the desired parts.
> A more user-friendly and powerful version of cut with sensible defaults.
> More information: <https://github.com/riquito/tuc>.

- Cut and rearrange fields:

`\n echo "foo bar baz" | tuc -d ' ' -f 3,2,1    # => bazbarfoo`

- Replace the delimiter `space` with an arrow:

`echo "foo bar baz" | tuc -d ' ' -r ' ➡ '`

- Keep a range of fields:

`echo "foo bar    baz" | tuc -d ' ' -f 2:   # => bar    baz`

- Cut using regular expressions:

`echo "a,b, c" | tuc -e '[, ]+' -f 1,3  # => ac`

- Emit JSON output:

`echo "foo bar baz" | tuc -d '{{ }}' --json`
