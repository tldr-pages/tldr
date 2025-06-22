# jello

> A command-line JSON processor using Python syntax.
> More information: <https://github.com/kellyjonbrazil/jello>.

- Pretty-print JSON or JSON-Lines data from `stdin` to `stdout`:

`jello < {{file.json}}`

- Output a schema of JSON or JSON Lines data from `stdin` to `stdout` (useful for grep):

`jello -s < {{file.json}}`

- Output all elements from arrays (or all the values from objects) in JSON or JSON-Lines data from `stdin` to `stdout`:

`jello -l < {{file.json}}`

- Output the first element in JSON or JSON-Lines data from `stdin` to `stdout`:

`jello _[0] < {{file.json}}`

- Output the value of a given key of each element in JSON or JSON-Lines data from `stdin` to `stdout`:

`jello '[i.{{key_name}} for i in _]' < {{file.json}}`

- Output the value of multiple keys as a new JSON object (assuming the input JSON has the keys `key_name1` and `key_name2`):

`jello '{"{{key1}}": _.{{key_name1}}, "{{key_name}}": _.{{key_name2}}}' < {{file.json}}`

- Output the value of a given key to a string (and disable JSON output):

`jello -r '"{{some text}}: " + _.{{key_name}}' < {{file.json}}`
