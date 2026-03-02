# ng test

> Run unit tests in a project.
> Note: Some commands might require additional packages such as Vitest.
> More information: <https://angular.dev/cli/test>.

- Run unit tests:

`ng {{[t|test]}}`

- Run unit tests using a specific configuration:

`ng {{[t|test]}} {{[-c|--configuration]}} {{development|production|...}}`

- Specify the browsers to use for test execution:

`ng {{[t|test]}} --browsers {{firefox|webkit|chromium}}`

- Enable code coverage:

`ng {{[t|test]}} --coverage`

- Generate a coverage report in a specific format:

`ng {{[t|test]}} --coverage --coverage-reporters {{cobertura|html|json|...}}`

- Enable debug mode for tests:

`ng {{[t|test]}} --debug`

- List all discovered test files without building or running tests:

`ng {{[t|test]}} --list-tests`
