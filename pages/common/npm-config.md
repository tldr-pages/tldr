# npm config

> Manage the npm configuration files.
> More information: <https://docs.npmjs.com/cli/v9/commands/npm-config>.

- Set configuration values - Updates the user configuration file with the specified key-value pairs:

`npm config set <key>=<value> [<key>=<value> ...]`

- Get configuration values - Echoes the specified config value(s) to stdout:

`npm config get [<key> [<key> ...]]`

- List all configuration settings - Displays all config settings, with options to show defaults and in JSON format:

`npm config list [--json]`

- Delete configuration keys - Removes specified keys from all configuration files:

`npm config delete <key> [<key> ...]`

- Edit configuration files - Opens the user or global config file in an editor:

`npm config edit`

- Fix invalid configuration items - Attempts to repair issues in the config:

`npm config fix`
