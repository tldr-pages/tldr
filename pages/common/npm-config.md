# npm-config

> Manage the `npm` configuration settings.
> More information: <https://docs.npmjs.com/cli/commands/npm-config>.

- Show all configuration settings:

`npm config list`

- List all configuration settings as `JSON`:

`npm config list --json`

- Get the value of a specific configuration key:

`npm config get {{key}}`

- Set a configuration key to a specific value:

`npm config set {{key}} {{value}}`

- Delete a configuration key:

`npm config delete {{key}}`

- Edit the global npm configuration file in the default editor:

`npm config edit`

- Attempt to repair invalid configuration items:

`npm config fix`
