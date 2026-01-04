# bun publish

> Publish a package to the bun registry.
> More information: <https://bun.com/docs/pm/cli/publish>.

- Publish the current package to the npm registry:

`bun publish`

- Publish a package from a specific directory:

`bun publish {{path/to/package_directory}}`

- Publish a scoped package with specific access level:

`bun publish --access {{public|restricted}}`

- Publish a package to a custom registry:

`bun publish --registry {{registry}}`

- Run a dry run to see what would be published without uploading:

`bun publish --dry-run`

- Publish a package with a specific distribution tag (e.g., alpha):

`bun publish --tag {{alpha}}`

- Publish with a one-time password for 2FA-enabled accounts:

`bun publish --otp {{one_time_password}}`

- Publish using a specific authentication type:

`bun publish --auth-type {{web|legacy}}`
