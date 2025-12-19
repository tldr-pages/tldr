# odpscmd auth

> User authorities in ODPS (Open Data Processing Service).
> See also: `odps`.
> More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- [Interactive] Add a user to the current project:

`add user {{username}};`

- [Interactive] Grant a set of authorities to a user:

`grant {{action_list}} on {{object_type}} {{object_name}} to user {{username}};`

- [Interactive] Show authorities of a user:

`show grants for {{username}};`

- [Interactive] Create a user role:

`create role {{role_name}};`

- [Interactive] Grant a set of authorities to a role:

`grant {{action_list}} on {{object_type}} {{object_name}} to role {{role_name}};`

- [Interactive] Describe authorities of a role:

`desc role {{role_name}};`

- [Interactive] Grant a role to a user:

`grant {{role_name}} to {{username}};`
