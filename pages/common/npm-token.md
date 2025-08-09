# npm token

> Manage and generate authentication tokens for the npm registry.
> More information: <https://docs.npmjs.com/cli/npm-token>.

- Create a new authentication token:

`npm token create`

- List all tokens associated with an account:

`npm token list`

- Delete a specific token using its token ID:

`npm token revoke {{token_id}}`

- Create a token with read-only access:

`npm token create --read-only`

- Create a token with publish access:

`npm token create --publish`

- Automatically configure an npm token in your global `.npmrc` file when you log in:

`npm login`

- Remove a token from the global configuration:

`npm token revoke {{token_id}}`
