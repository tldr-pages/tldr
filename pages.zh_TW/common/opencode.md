# opencode

> 一個用於程式設計的 AI 代理程式。
> 部分子命令（例如 `auth`、`models`、`web` 等）有各自的使用說明文件。
> 更多資訊：<https://opencode.ai/docs/cli/>。

- 啟動互動式終端使用者介面（TUI）：

`opencode`

- 繼續最近一次的工作階段：

`opencode {{[-c|--continue]}}`

- 直接傳入提示詞，以非互動模式執行 OpenCode：

`opencode run "{{提示詞}}"`

- 使用指定的模型與代理程式：

`opencode run {{[-m|--model]}} {{提供者}}/{{模型}} --agent {{代理程式名稱}} "{{提示詞}}"`

- 列出已設定提供者的所有可用模型：

`opencode models`

- 管理提供者的憑證與登入：

`opencode auth login`

- 啟動無介面的 OpenCode 伺服器以供 API 存取：

`opencode serve {{[-h|--hostname]}} {{主機名稱}} {{[-p|--port]}} {{連接埠}}`

- 使用自訂設定建立新的代理程式：

`opencode agent create`
