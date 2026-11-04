# terraform validate

> Validate the configuration files in a directory.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/validate>.

- Validate the configuration in the current directory:

`terraform validate`

- Output the validation result in JSON format:

`terraform validate -json`

- Validate the configuration without validating test files:

`terraform validate -no-tests`

- Validate the configuration in a specific directory:

`terraform validate {{path/to/directory}}`

- Validate the configuration using a custom test directory:

`terraform validate -test-directory {{path/to/test_directory}}`
