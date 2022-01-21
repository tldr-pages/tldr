# groupadd

> Add user groups to the system.
> See also: `groups`, `groupdel`, `groupmod`.
> More information: <https://manned.org/groupadd>.

- Create a new group:

`groupadd {{group_name}}`

- Create a new system group:

`groupadd --system {{group_name}}`

- Create a new group with the specific groupid:

`groupadd --gid {{id}} {{group_name}}`
