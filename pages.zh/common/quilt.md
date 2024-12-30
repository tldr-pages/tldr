# quilt

> 管理一系列补丁。
> 更多信息：<https://savannah.nongnu.org/projects/quilt>。

- 从文件导入现有补丁：

`quilt import {{path/to/filename.patch}}`

- 创建一个新的补丁：

`quilt new {{filename.patch}}`

- 将文件添加到当前补丁：

`quilt add {{path/to/file}}`

- 编辑文件后，使用更改刷新当前补丁：

`quilt refresh`

- 应用系列文件中的所有补丁：

`quilt push -a`

- 移除所有已应用的补丁：

`quilt pop -a`