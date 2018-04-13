# jq

> A lightweight and flexible command-line JSON processor.

- Output a JSON file, in pretty-print format:

`jq . {{file.json}}`

- Output all elements from arrays (or all key-value pairs from objects) in a JSON file:

`jq .[] {{file.json}}`

- Read JSON objects from a file into an array, and output it (inverse of `jq .[]`):

`jq --slurp . {{file.json}}`

- Output the first element in a JSON file:

`jq .[0] {{file.json}}`

- Output the value of a given key of the first element in a JSON from stdin:

`cat {{file.json}} | jq .[0].{{key_name}}`

- Output the value of a given key of each element in a JSON from stdin:

`cat {{file.json}} | jq 'map(.{{key_name}})'`
