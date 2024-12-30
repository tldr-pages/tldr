# setfacl

> 设置文件访问控制列表 (ACL)。
> 更多信息：<https://manned.org/setfacl>。

- [M]odify ACL of a file for user with read and write access:

`setfacl --modify u:{{用户名}}:rw {{文件或目录的路径}}`

- [M]odify [d]efault ACL of a file for all users:

`setfacl --modify --default u::rw {{文件或目录的路径}}`

- Remove ACL of a file for a user:

`setfacl --remove u:{{用户名}} {{文件或目录的路径}}`

- Remove all ACL entries of a file:

`setfacl --remove-all {{文件或目录的路径}}`