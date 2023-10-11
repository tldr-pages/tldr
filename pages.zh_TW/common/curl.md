# curl

> 向 / 從一個伺服器傳輸數據。
> 支持大多數協議，包括 HTTP、FTP 和 POP3.
> 更多資訊：<https://curl.se/docs/manpage.html>.

- 將指定 URL 的內容下載到檔案：

`curl {{http://example.com}} --output {{檔案/完整/路徑}}`

- 將檔案從 URL 保存到由 URL 指示的檔名：

`curl --remote-name {{http://example.com/filename}}`

- 下載檔案，跟隨重新導向，並且自動續傳（恢復）前序檔案傳輸：

`curl --remote-name --location --continue-at - {{http://example.com/filename}}`

- 發送表單編碼數據（`application/x-www-form-urlencoded` 的 POST 請求）：

`curl --data {{'name=bob'}} {{http://example.com/form}}`

- 發送帶有額外請求頭，使用自定義請求方法：

`curl --header {{'X-My-Header: 123'}} --request {{PUT}} {{http://example.com}}`

- 發送 JSON 格式的數據，並附加正確的 `Content-Type` 請求頭：

`curl --data {{'{"name":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- 透過使用者名稱和密碼訪問伺服器：

`curl --user myusername:mypassword {{http://example.com}}`

- 爲指定資源使用客戶端憑證和密鑰，並且跳過憑證驗證：

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
