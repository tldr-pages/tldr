# del

> 刪除一個或多個檔案。
> 在 PowerShell 中，此命令為 `Remove-Item` 的別名。本頁的描述是基於命令提示字元 (`cmd`) 中的 `del`。
> 更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- 查閱 PowerShell 的對應命令:

`tldr remove-item`

- 刪除一個或多個檔案 (可使用萬用字元)：

`del {{檔案1 檔案2 ...}}`

- 在刪除每個檔案之前提示確認：

`del {{檔案}} /p`

- 強制刪除唯讀檔案：

`del {{檔案}} /f`

- 遞歸刪除所有子目錄中的檔案：

`del {{檔案}} /s`

- 在使用全域萬用字元刪除檔案時不做提示確認：

`del {{檔案}} /q`

- 顯示幫助訊息和列出所有可用屬性：

`del /?`

- 刪除符合指定屬性的檔案：

`del {{檔案}} /a {{屬性}}`
