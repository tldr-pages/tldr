# agy

> Google 的代理式開發平台。
> 更多資訊：<https://antigravity.google/docs>。

- 開啟特定檔案或目錄：

`agy {{路徑/至/檔案或目錄}}`

- 比較兩個檔案：

`agy {{[-d|--diff]}} {{路徑/至/檔案1}} {{路徑/至/檔案2}}`

- 傳入提示詞來執行一個在目前工作目錄的聊天工作階段：

`agy chat "{{提示詞}}"`

- 安裝或解除安裝特定擴充功能：

`agy --{{install|uninstall}}-extension {{發布者.擴充功能|路徑/至/擴充功能.vsix}}`

- 向使用者設定檔案新增 MCP（Model Context Protocol）伺服器定義：

`agy --add-mcp "{{json_字串}}"`

- 顯示說明：

`agy {{[-h|--help]}}`
