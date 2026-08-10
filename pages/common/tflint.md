# tflint

> A pluggable Terraform linter to find errors, warn about deprecated syntax, and enforce best practices.
> More information: <https://github.com/terraform-linters/tflint>.

- Initialize plugin configuration and install declared plugins:

`tflint --init`

- Lint the Terraform configuration in the current directory:

`tflint`

- Lint with a specific config file:

`tflint --config {{path/to/.tflint.hcl}}`

- Run recursively in each subdirectory:

`tflint --recursive`

- Enable only a specific rule, disabling all other defaults:

`tflint --only {{rule_name}}`

- Disable a specific rule:

`tflint --disable-rule {{rule_name}}`

- Automatically fix issues where possible:

`tflint --fix`

- Output results in JSON format (useful for CI/CD):

`tflint --format json`
