# bun add

> Add dependencies to `package.json` and install them.
> More information: <https://bun.com/docs/cli/add>.

- Add a package as a dependency:

`bun add {{package_name}}`

- Add multiple packages as dependencies:

`bun add {{package1 package2 package3}}`

- Add a package as a development dependency:

`bun add --dev {{package_name}}`

- Add a package with a specific version:

`bun add {{package_name}}@{{version}}`

- Add a package globally:

`bun add --global {{package_name}}`

- Add a package from a Git repository:

`bun add {{git+https://github.com/user/repo.git}}`

- Add a package and save exact version:

`bun add --exact {{package_name}}`

- Add a package as an optional dependency:

`bun add --optional {{package_name}}`
