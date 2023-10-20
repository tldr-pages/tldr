# del

> 刪除一個或多個檔案。
> 更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- 刪除一個或多個以空格分隔的檔案：

`del {{檔案 檔案 ..}}`

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

`del {{檔案}} /a {{属性}}`
