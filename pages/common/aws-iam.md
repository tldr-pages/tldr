# aws iam

> CLI for AWS IAM.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- List users:

`aws iam list-users`

- List policies:

`aws iam list-policies`

- List groups:

`aws iam list-groups`

- Get users in a group:

`aws iam get-group --group-name {{group_name}}`

- Describe an IAM policy:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{policy_name}}`

- List access keys:

`aws iam list-access-keys`

- List access keys for a specific user:

`aws iam list-access-keys --user-name {{user_name}}`

- Display help:

`aws iam help`
