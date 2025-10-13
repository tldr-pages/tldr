# npm dist-tag

> Manage distribution tags on packages.
> More information: <https://docs.npmjs.com/cli/npm-dist-tag>.

- List all distribution tags for a package:

`npm dist-tag ls {{package_name}}`

- List all distribution tags for the current package:

`npm dist-tag ls`

- Add a distribution tag to a specific package version:

`npm dist-tag add {{package_name}}@{{version}} {{tag}}`

- Remove a distribution tag from a package:

`npm dist-tag rm {{package_name}} {{tag}}`

- Add a tag using the configured tag from npm config:

`npm dist-tag add {{package_name}}@{{version}}`

- Add a tag with two-factor authentication:

`npm dist-tag add {{package_name}}@{{version}} {{tag}} --otp {{one_time_password}}`
