# ng lint

> Check Angular project code for style and errors using the configured linter.
> More information: <https://angular.dev/cli/lint>.

- Lint all projects in the workspace:

`ng lint`

- Lint a specific project:

`ng lint {{project_name}}`

- Lint specific files:

`ng lint {{project_name}} --files {{path/to/file1.ts path/to/file2.ts ...}}`

- Exclude certain files or folders from linting:

`ng lint {{project_name}} --exclude {{pattern}}`

- Automatically fix linting errors:

`ng lint {{project_name}} --fix`

- Continue even if lint errors are found:

`ng lint {{project_name}} --force`

- Use a specific output format (e.g., stylish, json):

`ng lint {{project_name}} --format {{format}}`

- Specify a custom TypeScript configuration file:

`ng lint {{project_name}} --tsConfig {{path/to/tsconfig.json}}`
