# conda repoquery

> Advanced search for packages in a conda repository.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/repoquery/index.html>.

- Show available versions of the specified package:

`conda repoquery search {{package}}`

- Show dependencies of the specified package:

`conda repoquery depends {{package}}`

- Show packages that depend on the specified package:

`conda repoquery whoneeds {{package}}`
