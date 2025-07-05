# spf

> superfile – 現代的終端機檔案管理器。
> 更多資訊：<https://github.com/yorukot/superfile>.

- 使用指定路徑啟動 `spf`：

`spf {{path/to/start}}`

- 使用多個路徑啟動 `spf`：

`spf {{path/to/directory1 /path/to/directory2 ...}}`

- 修復快捷鍵設定，補上缺少的按鍵：

`spf {{[--fh|--fix-hotkeys]}}`

- 修復設定檔，補上缺少的項目：

`spf {{[--fch|--fix-config-file]}}`

- 使用指定的設定檔與快捷鍵檔案：

`spf {{[-c|--config-file]}} {{path/to/config.toml}} {{[--hf|--hotkey-file]}} {{path/to/hotkey.toml}}`

- 將第一個開啟的檔案路徑寫入該檔案並退出：

`spf {{[--cf|--chooser-file]}} {{tmp/chooser-result}}`

- 顯示內部設定與資料目錄路徑：

`spf {{[pl|path-list]}}`
