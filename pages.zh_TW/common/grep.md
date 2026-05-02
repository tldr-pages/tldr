# grep

> 使用 `regex` 式搜尋檔案中的模式。
> 另請參閱：`regex`。
> 更多資訊：<https://www.gnu.org/software/grep/manual/grep.html>。

- 在檔案中搜尋模式：

`grep "{{模式字串}}" {{路徑/至/檔案1 路徑/至/檔案2}}`

- 搜尋精確的字串（停用 `regex` 式）：

`grep {{[-F|--fixed-strings]}} "{{字串}}" {{路徑/至/檔案}}`

- 在目錄中遞迴搜尋所有檔案中的模式，忽略二進位檔案：

`grep {{[-rI|--recursive --binary-files=without-match]}} "{{模式字串}}" {{路徑/至/目錄}}`

- 列印每個匹配項周圍、之前或之後的 3 行上下文：

`grep {{--context|--before-context|--after-context}} 3 "{{模式字串}}" {{路徑/至/檔案}}`

- 列印每個匹配項的檔案名稱和行號，並帶彩色輸出：

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{模式字串}}" {{路徑/至/檔案}}`

- 僅列印匹配的文本：

`grep {{[-o|--only-matching]}} "{{模式字串}}" {{路徑/至/檔案}}`

- 從 `stdin` （標準輸入）中讀取資料，不列印匹配模式的行：

`cat {{路徑/至/檔案}} | grep {{[-v|--invert-match]}} "{{模式字串}}"`

- 使用擴展 `regex` 式（支援 `?`、`+`、`{}`、`()` 和 `|`），不區分大小寫模式：

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{模式字串}}" {{路徑/至/檔案}}`
