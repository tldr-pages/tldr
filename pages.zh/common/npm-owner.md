# npm owner

> 管理已发布包的所有权。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-owner>。

- 添加一个新用户作为包的维护者：

`npm owner add {{username}} {{package_name}}`

- 从包的所有者列表中移除一个用户：

`npm owner rm {{username}} {{package_name}}`

- 列出包的所有所有者：

`npm owner ls {{package_name}}`