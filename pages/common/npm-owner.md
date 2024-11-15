# npm owner

> Manage ownership of published packages.
> More information: <https://docs.npmjs.com/cli/commands/npm-owner>.

- Add a new user as a maintainer of a package:

`npm owner add {{username}} {{package_name}}`

- Remove a user from a package's owner list:

`npm owner rm {{username}} {{package_name}}`

- List all owners of a package:

`npm owner ls {{package_name}}`
