# jq

> A lightweight and flexible command-line JSON processor
 
- Output JSON file:

`jq '' {{file}}`
 
- Read JSON stream into array and output:

`jq -s '' {{file}}`

- Output first element in JSON file:

`jq '.[0]' {{file}}`

- Output "key" of first element in JSON file:

`jq '.[0].{{key}}' {{file}}`

- Output "key" of each element in JSON file:

`jq 'map(.{{key}})' {{file}}`
