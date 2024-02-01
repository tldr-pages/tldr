# jello

> A command-line JSON processor using Python syntax.
> More information: <https://github.com/kellyjonbrazil/jello>.

- Pretty-print JSON or JSON-Lines data from `stdin` to `stdout`:

`cat {{file.json}} | jello`

- Output a schema of JSON or JSON Lines data from `stdin` to `stdout` (useful for grep):

`cat {{file.json}} | jello -s`

- Output all elements from arrays (or all the values from objects) in JSON or JSON-Lines data from `stdin` to `stdout`:

`cat {{file.json}} | jello -l`

- Output the first element in JSON or JSON-Lines data from `stdin` to `stdout`:

`cat {{file.json}} | jello _[0]`

- Output the value of a given key of each element in JSON or JSON-Lines data from `stdin` to `stdout`:

`cat {{file.json}} | jello '[i.{{key_name}} for i in _]'`

- Output the value of multiple keys as a new JSON object (assuming the input JSON has the keys `key_name1` and `key_name2`):

`cat {{file.json}} | jello '{"{{key1}}": _.{{key_name1}}, "{{key_name}}": _.{{key_name2}}}'`

- Output the value of a given key to a string (and disable JSON output):

`cat {{file.json}} | jello -r '"{{some text}}: " + _.{{key_name}}'`
