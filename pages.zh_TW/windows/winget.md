# winget

> Windows 套件管理員的命令列工具。
> 更多資訊：<https://learn.microsoft.com/windows/package-manager/winget>.

- 安裝一個套件：

`winget install {{套件}}`

- 刪除一個套件（註：可以用 `remove` 代替 `uninstall`）：

`winget uninstall {{package}}`

- 顯示指定套件的相關資訊：

`winget show {{套件}}`

- 搜尋指定套件：

`winget search {{套件}}`

- 升級所有套件至最新版本：

`winget upgrade --all`

- 列出所有可由 `winget` 管理的已安裝套件：

`winget list --source winget`

- 從檔案匯入套件，或將已安裝的套件匯出至檔案：

`winget {{import|export}} {{--import-file|--output}} {{檔案/完整/路徑}}`

- 在提交 PR 到 winget-pkgs 存儲庫之前，請驗證 manifest 檔：

`winget validate {{manifest檔案/完整/路徑}}`
