# aws workmail

> Manage Amazon WorkMail.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/index.html>.

- List all WorkMail organizations:

`aws workmail list-organizations`

- List all users of a specific organization:

`aws workmail list-users --organization-id {{organization_id}}`

- Create a WorkMail user in a specific organization:

`aws workmail create-user --name {{username}} --display-name {{name}} --password {{password}} --organization-id {{organization_id}}`

- Register and enable a group/user to WorkMail:

`aws workmail register-to-work-mail --entity-id {{entity_id}} --email {{email}} --organization-id {{organization_id}}`

- Create a WorkMail group in a specific organization:

`aws workmail create-group --name {{group_name}} --organization-id {{organization_id}}`

- Associate a member to a specific group:

`aws workmail associate-member-to-group --group-id {{group_id}} --member-id {{member_id}} --organization-id {{organization_id}}`

- Deregister and disable a user/group from WorkMail:

`aws workmail deregister-from-work-mail --entity-id {{entity_id}} --organization-id {{organization_id}}`

- Delete a user from an organization:

`aws workmail delete-user --user-id {{user_id}} --organization-id {{organization_id}}`
