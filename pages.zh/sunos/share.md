# share

> 使本地资源/文件系统可供远程系统挂载。
> 更多信息：<https://docs.oracle.com/cd/E36784_01/html/E36825/gntjt.html>.

- 列出所有当前共享的文件系统：

`share`

- 共享一个具有读写权限的目录：

`share -F nfs -o rw {{/path/to/directory}}`

- 共享一个具有只读权限的目录：

`share -F nfs -o ro {{/path/to/directory}}`

- 共享一个具有特定选项的目录（例如，允许从特定主机进行根访问）：

`share -F nfs -o rw,root={{hostname}} {{/path/to/directory}}`

- 通过向 `/etc/dfs/dfstab` 添加条目使共享持久化：

`echo "share -F nfs -o rw {{/path/to/directory}}" >> /etc/dfs/dfstab`
