# odps auth

> User authorities in ODPS (Open Data Processing Service).

- Add a user to the current project:

`add user {{user_name}};`

- Grant a set of authorities to a user:

`grant {{action_list}} on {{object_type}} {{object_name}} to user {{user_name}};`

- Show authorities of a user:

`show grants for {{user_name}};`

- Create a user role:

`create role {{role_name}};`

- Grant a set of authorities to a role:

`grant {{action_list}} on {{object_type}} {{object_name}} to role {{role_name}};`

- Describe authorities of a role:

`desc role {{role_name}};`

- Grant a role to a user:

`grant {{role_name}} to {{user_name}};`
