# ng add

> Add and configure packages for the current workspace project.
> More information: <https://angular.dev/cli/add>.

- Add a package to the current project:

`ng add {{package}}`

- Add multiple packages:

`ng add {{package1 package2 ...}}`

- Add a specific version of a package:

`ng add {{package}}@{{version}}`

- Skip the confirmation prompt:

`ng add {{package}} --skip-confirmation`

- Disable interactive prompts:

`ng add {{package}} --interactive false`

- Display verbose output about internal operations:

`ng add {{package}} --verbose`

- Perform a dry run without making any changes:

`ng add {{package}} {{[-d|--dry-run]}}`
