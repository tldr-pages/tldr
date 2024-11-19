# jq

> A JSON processor that uses a domain-specific language (DSL).
> More information: <https://jqlang.github.io/jq/manual/>.

- Execute a specific expression (print a colored and formatted JSON output):

`{{cat path/to/file.json}} | jq '.'`

- Execute a specific script:

`{{cat path/to/file.json}} | jq --from-file {{path/to/script.jq}}`

- Pass specific arguments:

`{{cat path/to/file.json}} | jq {{--arg "name1" "value1" --arg "name2" "value2" ...}} '{{. + $ARGS.named}}'`

- Create new JSON object via an old JSON object:

`{{cat path/to/file.json}} | jq '{{{newKey1: .key1, newKey2: .key2.nestedKey, ...}}}'`

- Print specific array items:

`{{cat path/to/file.json}} | jq '{{.[index1], .[index2], ...}}'`

- Print all array/object values:

`{{cat path/to/file.json}} | jq '.[]'`

- Print multi-conditional objects in array:

`{{cat path/to/file.json}} | jq '.[] | select((.key1=="value1") and .key2=="value2")'`

- Add/remove specific keys:

`{{cat path/to/file.json}} | jq '. {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'`
