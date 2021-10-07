# az config

> Manage Azure CLI configuration.
> Part of `azure-cli`.
> More information: <https://docs.microsoft.com/cli/azure/config>.

- Print all configurations:

`az config get`

- Print configurations for a specific section:

`az config get {{section_name}}`

- Set a configuration:

`az config set {{configuration_name}}={{value}}`

- Unset a configuration:

`az config unset {{configuration_name}}`
