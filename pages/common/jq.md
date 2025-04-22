# jq

> A JSON processor that uses a domain-specific language (DSL).
> More information: <https://jqlang.github.io/jq/manual/>.

- Execute a specific expression only using the `jq` binary (print a colored and formatted JSON output):

`jq '.' {{/path/to/file.json}}`

- Execute a specific script:

`{{cat path/to/file.json}} | jq {{[-f|--from-file]}} {{path/to/script.jq}}`

- Pass specific arguments:

`{{cat path/to/file.json}} | jq {{--arg "name1" "value1" --arg "name2" "value2" ...}} '{{. + $ARGS.named}}'`

- Create new JSON object via old JSON objects from multiple files:

`{{cat path/to/multiple_json_file_*.json}} | jq '{{{newKey1: .key1, newKey2: .key2.nestedKey, ...}}}'`

- Print specific array items:

`{{cat path/to/file.json}} | jq '{{.[index1], .[index2], ...}}'`

- Print all array/object values:

`{{cat path/to/file.json}} | jq '.[]'`

- Print objects with 2-condition filter in array:

`{{cat path/to/file.json}} | jq '.[] | select((.key1=="value1") and .key2=="value2")'`

- Add/remove specific keys:

`{{cat path/to/file.json}} | jq '. {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'`
