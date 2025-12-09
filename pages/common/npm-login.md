# npm login

> Log in to a registry user account.
> See also: `npm logout` for logging out.
> More information: <https://docs.npmjs.com/cli/npm-login>.

- Log in to a registry user account and save the credentials to the `.npmrc` file:

`npm login`

- Log in using a custom registry:

`npm login --registry {{registry_url}}`

- Log in using a specific authentication strategy:

`npm login --auth-type {{legacy|web}}`
