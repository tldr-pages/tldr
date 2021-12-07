# terraform plan

> Generate and show Terraform execution plans.
> More information: <https://www.terraform.io/docs/cli/commands/plan.html>.

- Generate and show the execution plan in the currently directory:

`terraform plan`

- Show a plan to destroy all remote objects that currently exist:

`terraform plan -destroy`

- Show a plan to update the Terraform state and output values:

`terraform plan -refresh-only`

- Specify values for input variables:

`terraform plan -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Focus Terraform's attention on only a subset of resources:

`terraform plan -target {{resource_type.resource_name[instance index]}}`

- Output a plan as JSON:

`terraform plan -json`

- Write a plan to a specific file:

`terraform plan -no-color > {{path/to/file}}`
