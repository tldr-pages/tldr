# tflint

> A pluggable linter and validator for Terraform configuration files.
> More information: <https://tflint.io/docs/commands/>.

- Run TFLint in the current directory:

`tflint`

- Run TFLint in a specific directory:

`tflint --chdir {{path/to/directory}}`

- Run TFLint recursively in every subdirectory:

`tflint --recursive`

- Initialize TFLint, installing plugins defined in the configuration file:

`tflint --init`

- Run TFLint using a specific configuration file:

`tflint {{[-c|--config]}} {{path/to/config_file}}`

- Report issues in {{json}} format:

`tflint {{[-f|--format]}} {{json}}`

- Fix all issues that can be fixed automatically:

`tflint --fix`

- Display help:

`tflint --help`
