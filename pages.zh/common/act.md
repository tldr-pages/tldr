# act

> 使用 Docker 本地运行 GitHub Actions.
> 更多信息：<https://github.com/nektos/act>.

- 列出可用的 actions 清单：

`act -l`

- 运行默认 event：

`act`

- 运行指定 event：

`act {{事件类型}}`

- 运行指定 action：

`act -a {{action_id}}`

- 非实际运行 actions（也就是 dry-run 模式）：

`act -n`

- 展示详细记录：

`act -v`
