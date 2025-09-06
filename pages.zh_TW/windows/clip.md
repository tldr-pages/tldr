# clip

> 將輸入的內容複製到 Windows 剪貼簿中。
> 更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- 使用管道將命令輸出的內容複製到 Windows 剪貼簿中：

`{{dir}} | clip`

- 將文件內容複製到 Windows 剪貼簿中：

`clip < {{檔案/完整/路徑}}`

- 將帶有換行符的內容複製到 Windows 剪貼簿中：

`echo {{文字}} | clip`

- 將不帶換行符的內容複製到 Windows 剪貼簿中：

`echo | set /p="文字" | clip`
