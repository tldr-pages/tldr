# cat

> 印出並連接檔案內容。
> 更多資訊：<https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- 將檔案內容印出至 `stdout`:

`cat {{路徑/至/檔案}}`

- 連接多個檔案的內容並存至檔案中：

`cat {{路徑/至/檔案一 路徑/至/檔案二 ...}} > {{路徑/至/檔案}}`

- 連接多個檔案的內容並附加至檔案末端：

`cat {{路徑/至/檔案一 路徑/至/檔案二 ...}} >> {{路徑/至/檔案}}`

- 將 `stdin` 寫入檔案中:

`cat - > {{路徑/至/檔案}}`

- 輸出時標上行號：

`cat {{[-n|--number]}} {{路徑/至/檔案}}`

- 顯示不可列印及空白的字元（如果非 ASCII 的話則有 `M-` 的前綴）：

`cat {{[-vte|--show-nonprinting -t -e]}} {{路徑/至/檔案}}`
