# npm owner

> 管理已发布的包的所有权。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-owner>。

- 将新用户添加为包的维护者：

`npm owner add {{username}} {{package_name}}`

- 从包的所有者列表中移除用户：

`npm owner rm {{username}} {{package_name}}`

- 列出包的所有所有者：

`npm owner ls {{package_name}}`