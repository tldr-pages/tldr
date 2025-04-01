# gibo

> 获取 .gitignore 模板。
> 更多信息：<https://github.com/simonwhitaker/gibo>.

- 列出可用的模板：

`gibo list`

- 将模板写入 `stdout`：

`gibo dump {{boilerplate}}`

- 将模板写入 .gitignore：

`gibo dump {{boilerplate}} >>{{.gitignore}}`

- 搜索包含特定字符串的模板：

`gibo search {{string}}`

- 更新本地可用的模板：

`gibo update`