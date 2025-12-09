# poetry publish

> Publishes a package to a remote repository.
> More information: <https://python-poetry.org/docs/cli/#publish>.

- Publish the current package to PyPI:

`poetry publish`

- Build the package before publishing:

`poetry publish --build`

- Publish to a specific repository:

`poetry publish {{[-r|--repository]}} {{repository_name}}`

- Publish with specific credentials:

`poetry publish {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`

- Perform a dry run to see what would be done without actually publishing:

`poetry publish --dry-run`

- Skip files that already exist in the repository:

`poetry publish --skip-existing`
