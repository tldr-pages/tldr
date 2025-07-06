# grep

> 使用正則表達式在文件中查找字符串。
> 更多資訊：<https://www.gnu.org/software/grep/manual/grep.html>.

- 在檔案中尋找字符：

`grep "{{字符串}}" {{檔案/完整/路徑}}`

- 搜索確切的字符串(禁用正則表達式)：

`grep {{[-F|--fixed-strings]}} "{{精確字符串}}" {{檔案/完整/路徑}}`

- 在目錄中遞歸搜索模式，顯示匹配行的行號並忽略二進制文件：

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{字符串}}" {{檔案/完整/路徑}}`

- 使用擴展正則表達式(支持 `?`, `+`, `{}`, `()`, 和 `|`)，並啟用不區分大小寫的模式：

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{字符串}}" {{檔案/完整/路徑}}`

- 打印每次匹配的上下文、之前或之後的 3 行：

`grep {{--context|--before-context|--after-context}} 3 "{{字符串}}" {{檔案/完整/路徑}}`

- 打印包含匹配結果的文件名和行號，並啟用彩色輸出：

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{字符串}}" {{檔案/完整/路徑}}`

- 搜索與模式匹配的行，僅打印匹配的文本：

`grep {{[-o|--only-matching]}} "{{字符串}}" {{檔案/完整/路徑}}`

- 在標準輸入中搜索不匹配模式的行：

`cat {{檔案/完整/路徑}} | grep {{[-v|--invert-match]}} "{{字符串}}"`
