# aws cloud9

> Manage Cloud9 - a collection of tools to code, build, run, test, debug, and release software in the cloud.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/index.html>.

- List all Cloud9 development environment identifiers:

`aws cloud9 list-environments`

- Create a Cloud9 development environment:

`aws cloud9 create-environment-ec2 --name {{name}} --instance-type {{instance_type}}`

- Display information about Cloud9 development environments:

`aws cloud9 describe-environments --environment-ids {{environment_ids}}`

- Add an environment member to a Cloud9 development environment:

`aws cloud9 create-environment-membership --environment-id {{environment_id}} --user-arn {{user_arn}} --permissions {{permissions}}`

- Display status information for a Cloud9 development environment:

`aws cloud9 describe-environment-status --environment-id {{environment_id}}`

- Delete a Cloud9 environment:

`aws cloud9 delete-environment --environment-id {{environment_id}}`

- Delete an environment member from a development environment:

`aws cloud9 delete-environment-membership --environment-id {{environment_id}} --user-arn {{user_arn}}`
