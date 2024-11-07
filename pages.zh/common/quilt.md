# quilt

> 管理一系列补丁。
> 更多信息：<https://savannah.nongnu.org/projects/quilt>.

- 从文件中导入一个现有的补丁：

`quilt import {{路径/到/文件名.patch}}`

- 创建一个新补丁：

`quilt new {{文件名.patch}}`

- 将一个文件添加到当前补丁：

`quilt add {{路径/到/文件}}`

- 编辑文件后，使用更改刷新当前补丁：

`quilt refresh`

- 应用系列文件中的所有补丁：

`quilt push -a`

- 移除所有已应用的补丁：

`quilt pop -a`
