# aws

> The official CLI tool for Amazon Web Services.
> Wizard, SSO, Resource Autocompletion, and YAML options are v2 only.
> More information: <https://aws.amazon.com/cli>.

- Configure the AWS Command Line:

`aws configure wizard`

- Configure the AWS Command Line using SSO:

`aws configure sso`

- See help text for the AWS command:

`aws {{command}} help`

- Get the caller identity (used to troubleshoot permissions):

`aws sts get-caller-identity`

- List AWS resources in a region and output in yaml:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Use auto prompt to help with a command:

`aws iam create-user --cli-auto-prompt`

- Get an interactive wizard for an AWS resource:

`aws dynamodb wizard {{new_table}}`

- Generate a JSON CLI Skeleton (useful for infrastructure as code):

`aws dynamodb update-table --generate-cli-skeleton`
