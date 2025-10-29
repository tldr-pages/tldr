# conda-repoquery

> Query package information and relationships within a conda repository.
> Useful for exploring dependencies, versions, and reverse dependencies of packages.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/repoquery.html>.

- Search for a specific package across all available repositories:

`conda repoquery search {{package_name}}`

- Show all available versions of a package (including build numbers):

`conda repoquery search {{package_name}} --info`

- Show all dependencies required by a specific package:

`conda repoquery depends {{package_name}}`

- Show which packages depend on a specific package (reverse dependencies):

`conda repoquery whoneeds {{package_name}}`

- List all packages available in the current environment’s repositories:

`conda repoquery list`

- Show package details in JSON format (for use in scripts or automation):

`conda repoquery search {{package_name}} --json`
