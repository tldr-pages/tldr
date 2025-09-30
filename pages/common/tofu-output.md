# tofu output

> Export structured data about your OpenTofu resources.
> More information: <https://opentofu.org/docs/cli/commands/output/>.

- With no additional arguments, `output` will display all outputs for the root module:

`tofu output`

- Output only a value with specific name:

`tofu output {{name}}`

- Convert the output value to a raw string (useful for shell scripts):

`tofu output -raw`

- Format the outputs as a JSON object, with a key per output (useful with `jq`):

`tofu output -json`
