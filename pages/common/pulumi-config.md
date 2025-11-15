# pulumi config

> Manage configuration of a Pulumi stack.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_config/>.

- View current configuration in JSON format:

`pulumi config {{[-j|--json]}}`

- View configuration for a specified stack:

`pulumi config {{[-s|--stack]}} {{stack_name}}`

- Get the value of a configuration key:

`pulumi config get {{key}}`

- Remove a configuration value:

`pulumi config rm {{key}}`

- Set a value for a configuration key from a file:

`cat {{path/to/file}} | pulumi config set {{key}}`

- Set a secret value (e.g. API key) for a configuration key and store/display as ciphertext:

`pulumi config set --secret {{key}} {{S3cr37_value}}`

- Remove multiple configuration values from a specified configuration file:

`pulumi config --config-file {{path/to/file}} rm-all {{key1 key2 ...}}`
