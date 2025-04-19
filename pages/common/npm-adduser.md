# npm adduser

> Add a registry user account.
> More information: <https://docs.npmjs.com/cli/npm-adduser>.

- Create a new user in the specified registry and save credentials to `.npmrc`:

`npm adduser --registry {{registry_url}}`

- Log in to a private registry with a specific scope:

`npm login --scope {{@mycorp}} --registry {{https://registry.mycorp.com}}`

- Log out from a specific scope and remove the auth token:

`npm logout --scope {{@mycorp}}`

- Create a scoped package during initialization:

`npm init --scope {{@foo}} {{[-y|--yes]}}`
