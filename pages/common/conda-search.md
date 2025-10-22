# conda search

> Search for packages and show their details.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/search.html>.

- Search for a specific package:

`conda search {{package_name}}`

- Search for a package along with its details:

`conda search {{package_name}} {{[-i|--info]}}`

- Search for packages containing `string` in the package name:

`conda search "*{{string}}*"`

- Search for specific version of the package:

`conda search "{{package_name}}>={{package_version}}"`

- Search a package within a specific channel:

`conda search {{channel}}::{{package_name}}`

- Search if package is installed in any local environments:

`conda search --envs {{package_name}}`
