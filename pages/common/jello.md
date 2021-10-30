# jello

> A command-line JSON processor using Python syntax.
> More information: <https://github.com/kellyjonbrazil/jello>.

- Pretty-print JSON or JSON-Lines data from stdin to stdout:

`cat {{file.json}} | jello`

- Output a schema of JSON or JSON Lines data from stdin to stdout (useful for grep):

`cat {{file.json}} | jello -s`

- Output all elements from arrays (or all the values from objects) in JSON or JSON-Lines data from stdin to stdout:

`cat {{file.json}} | jello -l`

- Output the first element in JSON or JSON-Lines data from stdin to stdout:

`cat {{file.json}} | jello _[0]`

- Output the value of a given key of each element in JSON or JSON-Lines data from stdin to stdout:

`cat {{file.json}} | jello '[i.{{key_name}} for i in _]'`

- Output the value of multiple keys as a new JSON object (assuming the input JSON has the keys `key_name` and `other_key_name`):

`cat {{file.json}} | jello '{"{{my_new_key}}": _.{{key_name}}, "{{my_other_key}}": _.{{other_key_name}}}'`

- Output the value of a given key to a string (and disable JSON output):

`cat {{file.json}} | jello -r '"{{some text}}: " + _.{{key_name}}'`
