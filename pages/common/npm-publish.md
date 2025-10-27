# npm publish

> Publish a package to the npm registry.
> More information: <https://docs.npmjs.com/cli/publish>.

- Publish the current package to the default npm registry:

`npm publish`

- Publish a package from a specific directory:

`npm publish {{path/to/package_directory}}`

- Publish a scoped package with public access:

`npm publish --access public`

- Publish a scoped package with restricted (private) access:

`npm publish --access restricted`

- Publish a package to a custom registry:

`npm publish --registry {{https://registry.npmjs.org/}}`

- Run a dry run to see what would be published without uploading:

`npm publish --dry-run`

- Publish a package with a specific distribution tag (e.g., beta):

`npm publish --tag {{beta}}`

- Publish with a one-time password for 2FA-enabled accounts:

`npm publish --otp {{123456}}`
