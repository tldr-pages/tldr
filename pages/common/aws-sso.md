# aws sso

> Manage access to AWS resources using Single Sign-On (SSO) credentials.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso/index.html>.

- Start SSO session and refresh access tokens. Requires setup using `aws configure sso`:

`aws sso login`

- End SSO session and clear cached access tokens:

`aws sso logout`

- List all AWS accounts accessible to the user:

`aws sso list-accounts`

- List all roles accessible to the user for a given AWS account:

`aws sso list-account-roles --account-id {{account}} --access-token {{token}}`

- Retrieve short-term credentials for a specific account:

`aws get-role-credentials --account-id {{account}} --role-name {{role}} --access-token {{token}}`
