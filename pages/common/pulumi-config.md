# pulumi config

> Manage configuration.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_config/>.

- List all configuration values for a specific stack:

`pulumi config`

- Use the configuration values in the specified file rather than detecting the file name:

`pulumi config --config-file`

- Emit output as JSON:

`pulumi config --json`

- Open and resolve any environments listed in the stack configuration:

`pulumi config --open`

- Show secret values when listing config instead of displaying blinded values:

`pulumi config --show-secrets`

- The name of the stack to operate on. Defaults to the current stack:

`pulumi config --stack`
