# npm config

> Manage the `npm` configuration settings.
> More information: <https://docs.npmjs.com/cli/npm-config>.

- Show all configuration settings:

`npm {{[c|config]}} list`

- List all configuration settings as `JSON`:

`npm {{[c|config]}} list --json`

- Get the value of a specific configuration key:

`npm {{[c|config]}} get {{key}}`

- Set a configuration key to a specific value:

`npm {{[c|config]}} set {{key}} {{value}}`

- Delete a configuration key:

`npm {{[c|config]}} delete {{key}}`

- Edit the global npm configuration file in the default editor:

`npm {{[c|config]}} edit`

- Attempt to repair invalid configuration items:

`npm {{[c|config]}} fix`
