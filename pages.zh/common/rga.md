# rga

> Ripgrep 的带有丰富文件类型搜索能力的包装器。
> 更多信息：<https://github.com/phiresky/ripgrep-all>.

- 递归搜索当前目录中所有文件中的模式：

`rga {{正则表达式}}`

- 列出可用适配器：

`rga --rga-list-adapters`

- 更改使用的适配器（例如 ffmpeg, pandoc, poppler 等）：

`rga --rga-adapters={{adapter1,adapter2}} {{正则表达式}}`

- 使用文件的 MIME 类型而非扩展名搜索模式（较慢）：

`rga --rga-accurate {{正则表达式}}`

- 显示帮助：

`rga --help`