# alacritty

> 跨平台、GPU 加速的終端模擬器。
> 更多資訊：<https://manned.org/alacritty>。

- 啟動新的 Alacritty 程序並建立視窗：

`alacritty`

- 啟動 Alacritty 守護程序（不建立視窗）：

`alacritty --daemon`

- 使用已執行的 Alacritty 程序建立新視窗：

`alacritty msg create-window`

- 在指定目錄啟動 shell（也可搭配 `alacritty msg create-window` 使用）：

`alacritty --working-directory {{路徑/至/目錄}}`

- 執行（[e]xecute）命令到新 Alacritty 視窗（也可搭配 `alacritty msg create-window` 使用）：

`alacritty -e {{命令}}`

- 使用替代設定檔（預設使用 `$XDG_CONFIG_HOME/alacritty/alacritty.toml`）：

`alacritty --config-file {{路徑/至/設定.toml}}`

- 啟用即時設定重載執行（也可在 `alacritty.toml` 中預設啟用）：

`alacritty --live-config-reload --config-file {{路徑/至/設定.toml}}`
