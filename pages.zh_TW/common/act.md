# act

> 使用 Docker 在本機執行 GitHub Actions。
> 更多資訊：<https://manned.org/act>。

- 列出可用的 actions 清單：

`act -l`

- 執行預設 event：

`act`

- 執行指定 event：

`act {{event_type}}`

- 執行指定的 action：

`act -a {{action_id}}`

- 非實際執行 actions（也就是 dry-run 模式）：

`act -n`

- 顯示詳細記錄：

`act -v`

- 執行指定的 workflow：

`act push -W {{workflow 的路徑}}`
