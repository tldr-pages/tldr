# npm 版本

> 增加一个节点包的版本。
> 更多信息: <https://docs.npmjs.com/cli/commands/npm-version>。

- 检查当前版本：

`npm version`

- 增加次要版本：

`npm version minor`

- 设置特定版本：

`npm version {{version}}`

- 增加补丁版本而不创建 Git 标签：

`npm version patch --no-git-tag-version`

- 增加主要版本并自定义提交信息：

`npm version major -m "{{升级到 %s 的原因}}"`