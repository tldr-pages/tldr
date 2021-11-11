# terraform plan

> Generate and show an execution plan.
> More information: <https://www.terraform.io/docs/cli/commands/plan.html>.

- Generate and show an execution plan:

`terraform plan`

- Destroy mode - Show plan to destroy all remote objects that currently exist:

`terraform plan -destroy`

- Refresh-only mode - Show plan to update the Terraform state and output values:

`terraform plan -refresh-only`

- Specify values for input variables:

`terraform plan -var 'name=value'`

- Focus Terraform's attention on only a subset of resources:

`terraform plan -target resource_type.resource_name[instance index]`

- Output with JSON:

`terraform plan -json`

- Output plan to specific file:

`terraform plan -no-color >> plan.txt`
