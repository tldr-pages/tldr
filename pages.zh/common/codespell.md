# codespell

> 用于源代码的拼写检查工具。
> 更多信息：<https://github.com/codespell-project/codespell>。

- 检查当前目录中所有文本文件中的拼写错误，递归执行：

`codespell`

- 在原地纠正所有找到的拼写错误：

`codespell --write-changes`

- 跳过名称匹配指定模式的文件（接受逗号分隔的模式列表，支持通配符）：

`codespell --skip "{{pattern}}"`

- 在检查时使用自定义词典文件（`--dictionary` 可以多次使用）：

`codespell --dictionary {{path/to/file.txt}}`

- 不检查指定文件中列出的单词：

`codespell --ignore-words {{path/to/file.txt}}`

- 不检查指定的单词：

`codespell --ignore-words-list {{ignored_word1,ignored_word2,...}}`

- 在每个匹配项前后打印 3 行上下文：

`codespell --{{context|before-context|after-context}} {{3}}`

- 除了文件内容外，还检查文件名中的拼写错误：

`codespell --check-filenames`
