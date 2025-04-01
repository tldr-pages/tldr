# flow

> 一个用于 JavaScript 的静态类型检查器。
> 更多信息：<https://flow.org>。

- 运行 flow 检查：

`flow`

- 检查 flow 正在检查哪些文件：

`flow ls`

- 运行一个类型覆盖率检查，涵盖目录中的所有文件：

`flow batch-coverage --show-all --strip-root {{path/to/directory}}`

- 显示逐行的类型覆盖率统计信息：

`flow coverage --color {{path/to/file.jsx}}`