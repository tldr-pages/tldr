# npm search

> Search for packages in the `npm` registry.
> More information: <https://docs.npmjs.com/cli/commands/npm-search>.

- Search for a package by name:

`npm search {{package}}`

- Search for packages by a specific keyword:

`npm search {{keyword}}`

- Search for packages, including detailed information (e.g., description, author, version):

`npm search {{package}} --long`

- Search for packages maintained by a specific author:

`npm search --author {{author}}`

- Search for packages with a specific organization:

`npm search --scope {{organization}}`

- Search for packages with a specific combination of terms:

`npm search {{term1 term2 ...}}`
