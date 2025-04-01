# setfacl

> 设置文件访问控制列表 (ACL)。
> 更多信息： <https://manned.org/setfacl>。

- 修改文件的 ACL，为用户设置读写权限：

`setfacl {{[-m|--modify]}} u:{{username}}:rw {{path/to/file_or_directory}}`

- 修改文件的默认 ACL，为所有用户设置读写权限：

`setfacl {{[-m|--modify]}} {{[-d|--default]}} u::rw {{path/to/file_or_directory}}`

- 移除文件的 ACL 中指定用户的权限：

`setfacl {{[-x|--remove]}} u:{{username}} {{path/to/file_or_directory}}`

- 移除文件的所有 ACL 条目：

`setfacl {{[-X|--remove-all]}} {{path/to/file_or_directory}}`
