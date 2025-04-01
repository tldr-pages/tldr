# csslint

> 检查 CSS 代码。
> 更多信息：<https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- 检查单个 CSS 文件：

`csslint {{file.css}}`

- 检查多个 CSS 文件：

`csslint {{file1.css file2.css ...}}`

- 列出所有可能的样式规则：

`csslint --list-rules`

- 将某些规则视为错误（导致非零退出代码）：

`csslint --errors={{errors,universal-selector,imports}} {{file.css}}`

- 将某些规则视为警告：

`csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}`

- 忽略特定的规则：

`csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}`