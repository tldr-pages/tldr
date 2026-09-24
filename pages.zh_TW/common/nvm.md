# nvm

> 安裝、解除安裝或切換 Node.js 版本。
> 支援如 "12.8" 或 "v16.13.1" 等版本號，以及 "node"、"system" 等標籤。
> 另請參閱：`asdf`。
> 更多資訊：<https://github.com/nvm-sh/nvm#usage>。

- 安裝/解除安裝指定版本的 Node.js：

`nvm {{install|uninstall}} {{node_版本}}`

- 在目前 shell 中使用指定版本的 Node.js：

`nvm use {{node_版本}}`

- 設定預設的 Node.js 版本：

`nvm alias default {{node_版本}}`

- 列出可安裝的遠端版本，僅顯示 LTS（長期支援）版本：

`nvm ls-remote --lts`

- 列出已安裝的版本：

`nvm {{[ls|list]}}`

- 啟動指定版本 Node.js 的互動式命令列：

`nvm run {{node_版本}}`

- 使用指定版本的 Node.js 執行指令碼：

`nvm exec {{node_版本}} node {{路徑/到/指令碼.js}}`

- 在目前 Node.js 版本上升級到最新的可用 npm 版本：

`nvm install-latest-npm`
