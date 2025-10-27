# npm-ping

> Ping the configured or given npm registry and verify authentication.
> More information: <https://docs.npmjs.com/cli/commands/npm-ping>.

- Ping the default npm registry:

`npm ping`

- Ping custom npm registry:

`npm ping --registry {{custom_registry_url}}`

- Ping a private registry with an authentication token:

`npm ping --registry {{private_registry_url}} --_authToken={{TOKEN}}`
