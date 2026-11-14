# terraform test

> Execute integration and unit tests for Terraform configurations.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/test>.

- Run all tests in the current module:

`terraform test`

- Run tests from a specific directory:

`terraform test -test-directory={{path/to/directory}}`

- Run only tests in a specific test file:

`terraform test -filter={{path/to/test_file.tftest.hcl}}`

- Output test results in JSON format:

`terraform test -json`

- Generate a test report in JUnit XML format:

`terraform test -junit-xml={{path/to/results.xml}}`

- Display verbose execution logs during test execution:

`terraform test -verbose`
