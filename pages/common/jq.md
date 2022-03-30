# jq

> A command-line JSON processor that uses a domain-specific language.
> More information: <https://stedolan.github.io/jq/manual/>.

- Execute the specified expression:

`{{json_output_command}} | jq '{{.}}'`

- Execute the specified script:

`{{json_output_command}} | jq --from-file {{path/to/script.jq}}'`

- Print a colored and formatted json:

`{{json_output_command}} | jq '{{.}}'`

- Print the specifed key:

`{{json_output_command}} | jq '.{{key}}'`

- Print the specifed array item:

`{{json_output_command}} | jq '.[{{index}}]'`

- Print all array items/object keys:

`{{json_output_command}} | jq '.[]'`

- Add/remove the specified keys:

`{{json_output_command}} | jq '{{.}} {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'`
