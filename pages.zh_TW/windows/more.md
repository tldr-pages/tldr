# more

> 分頁顯示標準輸入或文件的輸出。
> 更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- 分頁顯示標準輸入的輸出：

`{{echo test}} | more`

- 分頁顯示一個或多個文件的內容：

`more {{檔案/完整/路徑}}`

- 將製表符（tab）轉換為指定的空格數（space）：

`more {{檔案/完整/路徑}} /t{{空格數}}`

- 顯示內容前先清除輸出：

`more {{檔案/完整/路徑}} /c`

- 從第 5 行開始顯示輸出：

`more {{檔案/完整/路徑}} +{{5}}`

- 啟用擴展交互模式（請參閱使用幫助）：

`more {{檔案/完整/路徑}} /e`

- 顯示全部幫助資訊：

`more /?`
