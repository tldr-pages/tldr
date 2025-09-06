# terraform output

> Export structured data about your Terraform resources.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/output>.

- With no additional arguments, `output` will display all outputs for the root module:

`terraform output`

- Output only a value with specific name:

`terraform output {{name}}`

- Convert the output value to a raw string (useful for shell scripts):

`terraform output -raw`

- Format the outputs as a JSON object, with a key per output (useful with jq):

`terraform output -json`
