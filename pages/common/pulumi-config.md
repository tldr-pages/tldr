# pulumi config

> Manage configuration for a Pulumi stack.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_config/>.

- View current configuration in JSON format:

`pulumi config --json`

- Get the value of a configuration key:

`pulumi config get {{key}}`

- Remove a configuration value:

`pulumi config rm {{key}}`

- Set value for a key from a file:

`cat {{path/to/file}} | pulumi config set {{key}}`

- Set secret value (e.g. API key) for a key and store/display as ciphertext:

`pulumi config set --secret {{key}} {{S3cr37_value}}`

- Remove multiple configuration values from a specified configuration file:

`pulumi config --config-file {{path/to/file}} rm-all {{key1 key2 ...}}`
