# rga

> 一个具有丰富文件类型搜索功能的Ripgrep包装器。
> 更多信息：<https://github.com/phiresky/ripgrep-all>。

- 在当前目录中的所有文件中递归搜索模式：

`rga {{正则表达式}}`

- 列出可用的适配器：

`rga --rga-list-adapters`

- 更改要使用的适配器（例如ffmpeg、pandoc、poppler等）：

`rga --rga-adapters={{适配器1,适配器2}} {{正则表达式}}`

- 使用MIME类型而不是文件扩展名搜索模式（速度较慢）：

`rga --rga-accurate {{正则表达式}}`

- 显示帮助：

`rga --help`