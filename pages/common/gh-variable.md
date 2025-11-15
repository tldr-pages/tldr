# gh variable

> Manage GitHub Actions and Dependabot variables.
> More information: <https://cli.github.com/manual/gh_variable>.

- List variables for the current repository:

`gh variable {{[ls|list]}}`

- List variables for a specific organization:

`gh variable {{[ls|list]}} {{[-o|--org]}} {{organization}}`

- Get a variable for the current repository:

`gh variable get {{name}}`

- Set a variable for the current repository (user will be prompted for the value):

`gh variable set {{name}}`

- Set a variable for a deployment environment in the current repository:

`gh variable set {{name}} {{[-e|--env]}} {{environment_name}}`

- Set an organization variable visible to all repositories:

`gh variable set {{name}} {{[-o|--org]}} {{organization}} {{[-v|--visibility]}} all`

- Set multiple variables from a dotenv file:

`gh variable set {{[-f|--env-file]}} {{path/to/file.env}}`

- Delete a variable for the current repository:

`gh variable delete {{name}}`
