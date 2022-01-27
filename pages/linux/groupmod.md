# groupmod

> Modify existing user groups in the system.
> See also: `groups`, `groupadd`, `groupdel`.
> More information: <https://manned.org/groupmod>.

- Change the group name:

`sudo groupmod --new-name {{new_group}} {{group_name}}`

- Change the group id:

`sudo groupmod --gid {{new_id}} {{group_name}}`
