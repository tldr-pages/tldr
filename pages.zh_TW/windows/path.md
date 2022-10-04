# path

> 顯示或設定可執行檔的搜尋路徑。
> 更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/path>.

- 顯示當前的 PATH 環境變數的設定：

`path`

- 將路徑設定為一個或多個以分號分隔的路徑目錄：

`path {{檔案/完整/路徑}};{{檔案/完整/路徑]}}`

- 將新的路徑目錄附加到到原始路徑：

`path {{檔案/完整/路徑}};%path%`

- 將命令提示字元設定為僅在當前目錄中搜尋可執行檔：

`path ;`
