# zapier 转换

> 将可视化构建器集成转换为 CLI 集成。
> 更多信息： <https://platform.zapier.com/reference/cli#convert>。

- 转换可视化构建器集成：

`zapier convert {{integration_id}} {{path/to/directory}}`

- 转换具有特定版本的可视化构建器集成：

`zapier convert {{integration_id}} {{path/to/directory}} {{-v|--version}}={{version}}`

- 显示额外的调试输出：

`zapier convert --debug`