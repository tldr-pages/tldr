# jq

> A command-line JSON processor that uses a domain-specific language.
> More information: <https://stedolan.github.io/jq/manual/>.

- Execute the specified expression (print a colored and formatted json):

`{{cat path/to/file.json}} | jq '{{.}}'`

- Execute the specified script:

`{{cat path/to/file.json}} | jq --from-file {{path/to/script.jq}}'`

- Pass the specifed arguments:

`{{cat path/to/file.json}} | jq {{--arg "name1" "value1" --arg "name2" "value2" ...}} '{{. + $ARGS.named}}'`

- Print the specifed keys:

`{{cat path/to/file.json}} | jq '{{.key1, .key2, ...}}'`

- Print the specifed array items:

`{{cat path/to/file.json}} | jq '{{.[index1], .[index2], ...}}'`

- Print all array items/object keys:

`{{cat path/to/file.json}} | jq '.[]'`

- Add/remove the specified keys:

`{{cat path/to/file.json}} | jq '{{.}} {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'`
