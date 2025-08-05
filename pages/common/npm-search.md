# npm search

> Search for packages in the `npm` registry.
> More information: <https://docs.npmjs.com/cli/npm-search>.

- Search for a package by name:

`npm {{[s|search]}} {{package}}`

- Search for packages by a specific keyword:

`npm {{[s|search]}} {{keyword}}`

- Search for packages, including detailed information (e.g., description, author, version):

`npm {{[s|search]}} {{package}} --long`

- Search for packages maintained by a specific author:

`npm {{[s|search]}} --author {{author}}`

- Search for packages with a specific organization:

`npm {{[s|search]}} --scope {{organization}}`

- Search for packages with a specific combination of terms:

`npm {{[s|search]}} {{term1 term2 ...}}`
