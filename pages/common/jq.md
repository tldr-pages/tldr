# jq

> A lightweight and flexible command-line JSON processor.

- Output JSON file:

`cat {{file}} | jq`

- Output all elements from JSON array in file, or all key-value pairs from JSON objects in file:

`cat {{file}} | jq .[]`

- Read JSON objects from file, into array, and output (inverse of `jq .[]`):

`cat {{file}} | jq --slurp`

- Output first element in JSON file:

`cat {{file}} | jq .[0]`

- Output "key" of first element in JSON file:

`cat {{file}} | jq .[0].{{key}}`

- Output "key" of each element in JSON file:

`cat {{file}} | jq 'map(.{{key}})'`
