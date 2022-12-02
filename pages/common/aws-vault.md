# aws-vault

> A vault for securely storing and accessing AWS credentials in development environments.
> More information: <https://github.com/99designs/aws-vault>.

- Add credentials to the secure keystore:

`aws-vault add {{path/to/file}}`

- Execute a command with AWS credentials in the environment:

`aws-vault exec {{path/to/file}} -- {{aws s3 ls}}`

- Open a browser window and login to the AWS Console:

`aws-vault login {{path/to/file}}`

- List profiles, along with their credentials and sessions:

`aws-vault list`

- Rotate AWS credentials:

`aws-vault rotate {{path/to/file}}`

- Remove credentials from the secure keystore:

`aws-vault remove {{path/to/file}}`
