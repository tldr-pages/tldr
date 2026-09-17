# terraform console

> Start an interactive console for evaluating Terraform expressions.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/console>.

- Start an interactive console to evaluate expressions:

`terraform console`

- Evaluate expressions against the planned state instead of current state:

`terraform console -plan`

- Evaluate a specific expression non-interactively:

`echo "{{expression}}" | terraform console`

- Specify values for input variables:

`terraform console -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Specify values for input variables from a file:

`terraform console -var-file {{path/to/file.tfvars}}`
