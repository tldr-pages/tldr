# find

> 在一個或多個文件中查詢指定字串。
> 更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- 查詢包含指定字串的行：

`find {{字串}} {{檔案或目錄/完整/路徑}}`

- 查詢不包含指定字串的行：

`find {{字串}} {{檔案或目錄/完整/路徑}} /v`

- 顯示包含指定字串的行總數：

`find {{字串}} {{檔案或目錄/完整/路徑}} /c`

- 顯示符合的行號：

`find {{字串}} {{檔案或目錄/完整/路徑}} /n`
