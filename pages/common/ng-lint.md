# ng lint

> Check Angular project code for style and errors using the configured linter.
> Note: Linting requires setup via `ng add`.
> More information: <https://angular.dev/cli/lint>.

- Lint all projects in the workspace:

`ng lint`

- Lint a specific project:

`ng lint {{project_name}}`

- Automatically fix linting errors:

`ng lint {{project_name}} --fix`

- Return a successful exit code even if lint errors are found:

`ng lint {{project_name}} --force`

- Use a specific output format:

`ng lint {{project_name}} --format {{stylish|json|...}}`
