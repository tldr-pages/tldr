# jq

> A lightweight and flexible command-line JSON processor.

- Output a JSON file, in pretty-print format:

`cat {{file}} | jq`

- Output all elements from arrays (or all key-value pairs from objects) in a JSON file:

`cat {{file}} | jq .[]`

- Read JSON objects from a file into an array, and output it (inverse of `jq .[]`):

`cat {{file}} | jq --slurp`

- Output the first element in a JSON file:

`cat {{file}} | jq .[0]`

- Output the value of a given key of the first element in a JSON file:

`cat {{file}} | jq .[0].{{key_name}}`

- Output the value of a given key of each element in a JSON file:

`cat {{file}} | jq 'map(.{{key_name}})'`
