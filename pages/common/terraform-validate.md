# terraform validate

> Check whether the configuration in a Terraform working directory is syntactically valid and internally consistent.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/validate>.

- Validate the configuration files in the current directory:

`terraform validate`

- Validate and output the result in JSON format (useful for parsing in CI):

`terraform validate -json`

- Validate without color codes in the output:

`terraform validate -no-color`

- Validate without running tests defined in `.tftest.hcl` files:

`terraform validate -no-tests`

- Validate using a custom directory for test files:

`terraform validate -test-directory={{path/to/tests}}`
