# grep

> 使用正則表達式在文件中查找字串。
> 更多資訊：<https://www.gnu.org/software/grep/manual/grep.html>.

- 在檔案中尋找字串：

`grep "{{字串}}" {{檔案/完整/路徑}}`

- 搜索確切的字串(停用正則表達式)：

`grep {{[-F|--fixed-strings]}} "{{精確字串}}" {{檔案/完整/路徑}}`

- 在目錄中遞迴搜尋模式，顯示相符行的行號並忽略二進位文件：

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{字串}}" {{檔案/完整/路徑}}`

- 使用擴充正則表達式(支援 `?`, `+`, `{}`, `()`, 和 `|`)，並啟用不區分大小寫的模式：

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{字串}}" {{檔案/完整/路徑}}`

- 印出每次相符的上下文、之前或之後的 3 行：

`grep {{--context|--before-context|--after-context}} 3 "{{字串}}" {{檔案/完整/路徑}}`

- 印出包含相符結果的文件名和行號，並啟用彩色輸出：

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{字串}}" {{檔案/完整/路徑}}`

- 搜尋與模式相符的行，僅印出相符的文字：

`grep {{[-o|--only-matching]}} "{{字串}}" {{檔案/完整/路徑}}`

- 在標準輸入中搜尋不相符模式的行：

`cat {{檔案/完整/路徑}} | grep {{[-v|--invert-match]}} "{{字串}}"`
