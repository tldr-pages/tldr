# aws configure

> Configure AWS CLI options.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Configure AWS CLI interactively (creates a new configuration or updates the default):

`aws configure`

- Configure a named profile for AWS CLI interactively (creates a new profile or updates an existing one):

`aws configure --profile {{production}}`

- Display the value from a specific configuration variable:

`aws configure get {{name}}`

- Display the value for a configuration variable in a specific profile:

`aws configure get {{name}} --profile {{profile_name}}`

- Set the value of a specific configuration variable:

`aws configure set {{name}} {{value}}`

- Set a configuration value from a profile configuration file:

`aws configure set {{name}} {{value}} --profile {{profile_name}}`

- List the AWS CLI configuration data:

`aws configure list`

- List the AWS CLI profile configuration data:

`aws configure list --profile {{production}}`
