# odps authority

> Manaage authorities in ODPS (Open Data Processing Service).

- Show authorities of a user:

`show grants for {{account_name}};`

- Add user to current project:

`add user {{account_name}};`

- Grant a set of authorities to a user:

`grant {{action_list}} on {{object}} {{object_name}} to user {{account_name}};`

- Create a role:

`create role {{role_name}};`

- Grant a set of authorities to a role:

`grant {{action_list}} on {{object}} {{object_name}} to role {{role_name}};`

- Grant a role to a user:

`grant {{role_name}} to {{user_name}};`
