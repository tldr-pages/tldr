# setfacl

> Set file access control lists (ACL).
> More information: <https://manned.org/setfacl>.

- Modify ACL of a file for user with read and write access:

`setfacl -m u:{{username}}:rw {{path/to/file}}`

- Modify default ACL of a file for all users:

`setfacl -d -m u::rw {{path/to/file}}`

- Remove ACL of a file for a user:

`setfacl -x u:{{username}} {{path/to/file}}`

- Remove all ACL entries of a file:

`setfacl -b {{path/to/file}}`
