# rlwrap

> 为 REPL 命令添加行编辑、持久历史和提示补全功能。
> 更多信息：<https://github.com/hanslub42/rlwrap>。

- 运行具有行编辑、持久历史和提示补全的 REPL 命令：

`rlwrap {{command}}`

- 使用输入和输出中看到的所有单词进行提示补全：

`rlwrap --remember {{command}}`

- 如果提示包含 ANSI 颜色代码，则提示补全效果更佳：

`rlwrap --ansi-colour-aware {{command}}`

- 启用文件名补全（区分大小写）：

`rlwrap --complete-filenames {{command}}`

- 添加彩色提示，使用颜色名称或符合 ASCII 的颜色规格。使用大写颜色名称来实现加粗样式：

`rlwrap --prompt-colour={{black|red|green|yellow|blue|cyan|purple|white|colour_spec}} {{command}}`