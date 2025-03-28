# setfacl

> Set file access control lists (ACL).
> More information: <https://manned.org/setfacl>.

- Modify ACL of a file for user with read and write access:

`setfacl {{[-m|--modify]}} u:{{username}}:rw {{path/to/file_or_directory}}`

- Modify default ACL of a file for all users:

`setfacl {{[-m|--modify]}} {{[-d|--default]}} u::rw {{path/to/file_or_directory}}`

- Remove ACL of a file for a user:

`setfacl {{[-x|--remove]}} u:{{username}} {{path/to/file_or_directory}}`

- Remove all ACL entries of a file:

`setfacl {{[-X|--remove-all]}} {{path/to/file_or_directory}}`
