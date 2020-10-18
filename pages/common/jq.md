# jq

> A command-line JSON processor that uses a domain-specific language.
> More information: <https://stedolan.github.io/jq>.

- Output a JSON file, in pretty-print format:

`jq . {{file.json}}`

- Output all elements from arrays (or all the values from objects) in a JSON file:

`jq '.[]' {{file.json}}`

- Read JSON objects from a file into an array, and output it (inverse of `jq .[]`):

`jq --slurp . {{file.json}}`

- Output a value under given path. The path can consist of array indices (wrapped with `[]`) and object keys:

`jq '.{{key_name}}.[{{index}}].{{another_key}}' {{file.json}}`

- Output the value of a given key of each element in a JSON text from `stdin`:

`cat {{file.json}} | jq 'map(.{{key_name}})'`

- Output the value of multiple keys as a new JSON object (assuming the input JSON has the keys `key_name` and `other_key_name`):

`cat {{file.json}} | jq '{{{my_new_key}}: .{{key_name}}, {{my_other_key}}: .{{other_key_name}}}'`

- Combine multiple filters:

`cat {{file.json}} | jq 'unique | sort | reverse'`

- Output the value of a given key to a string (and disable JSON output):

`cat {{file.json}} | jq --raw-output '"some text: \(.{{key_name}})"'`

- Output the value of a given key from a JSON parsable lines, and skip if parsing is not successful:

`cat {{file.json}} | jq --raw-input 'fromjson? | .{{key_name}}'`
