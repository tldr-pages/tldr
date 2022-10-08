# aws configure

> Configure AWS CLI options.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Configure AWS CLI interactively (creates a new configuration or updates the default):

`aws configure`

- Configure a named profile for AWS CLI interactively (new profile or updating the existing):

`aws configure --profile {{production}}`

- Get a configuration value from the configuration file:

`aws configure get {{region}}`

- Get a configuration value from a profile configuration file:

`aws configure get {{region}} --profile {{production}}`

- Set a configuration value from the configuration file:

`aws configure set {{region}} {{us-west-1}}`

- Set a configuration value from a profile configuration file:

`aws configure set {{region}} {{us-west-1}} --profile {{production}}`

- List the AWS CLI configuration data:

`aws configure list`

- List the AWS CLI profile configuration data:

`aws configure list --profile {{production}}`
