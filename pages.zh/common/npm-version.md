# npm version

> 更新 Node 包的版本。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-version>。

- 查看当前版本：

`npm version`

- 更新次版本号：

`npm version minor`

- 设置特定版本号：

`npm version {{version}}`

- 更新修订版本号但不创建 Git 标签：

`npm version patch --no-git-tag-version`

- 更新主版本号并使用自定义提交消息：

`npm version major -m "{{升级到 %s 以解决某些问题}}"`