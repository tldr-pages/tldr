# codespell

> 源代码拼写检查工具。
> 更多信息：<https://github.com/codespell-project/codespell>。

- 递归检查当前目录下所有文本文件中的拼写错误：

`codespell`

- 在原地修正所有发现的拼写错误：

`codespell --write-changes`

- 跳过与指定模式匹配的文件（接受使用通配符的逗号分隔模式列表）：

`codespell --skip "{{pattern}}"`

- 检查时使用自定义字典文件（`--dictionary` 可以多次使用）：

`codespell --dictionary {{path/to/file.txt}}`

- 不检查在指定文件中列出的单词：

`codespell --ignore-words {{path/to/file.txt}}`

- 不检查指定的单词：

`codespell --ignore-words-list {{ignored_word1,ignored_word2,...}}`

- 在每个匹配项前后打印 3 行上下文：

`codespell --{{context|before-context|after-context}} {{3}}`

- 除了文件内容外，还检查文件名中的拼写错误：

`codespell --check-filenames`