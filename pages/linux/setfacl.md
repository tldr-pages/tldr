# setfacl

> Set file access control lists (ACL).
> More information: <https://manned.org/setfacl>.

- [M]odify ACL of a file for user with read and write access:

`setfacl --modify u:{{username}}:rw {{path/to/file_or_directory}}`

- [M]odify [d]efault ACL of a file for all users:

`setfacl --modify --default u::rw {{path/to/file_or_directory}}`

- Remove ACL of a file for a user:

`setfacl --remove u:{{username}} {{path/to/file_or_directory}}`

- Remove all ACL entries of a file:

`setfacl --remove-all {{path/to/file_or_directory}}`
