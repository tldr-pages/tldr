# aws configure

> Manage configuration for the AWS CLI.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Configure AWS CLI interactively (creates a new configuration or updates the default):

`aws configure`

- Configure a named profile for AWS CLI interactively (creates a new profile or updates an existing one):

`aws configure --profile {{path/to/file}}`

- Display the value from a specific configuration variable:

`aws configure get {{name}}`

- Display the value for a configuration variable in a specific profile:

`aws configure get {{name}} --profile {{path/to/file}}`

- Set the value of a specific configuration variable:

`aws configure set {{name}} {{value}}`

- Set the value of a configuration variable in a specific profile:

`aws configure set {{name}} {{value}} --profile {{path/to/file}}`

- List the configuration entries:

`aws configure list`

- List the configuration entries for a specific profile:

`aws configure list --profile {{path/to/file}}`
