# rlwrap

> 为 REPL 命令添加行编辑、持久历史记录和提示补全功能。
> 更多信息：<https://github.com/hanslub42/rlwrap>。

- 运行具有行编辑、持久历史记录和提示补全功能的 REPL 命令：

`rlwrap {{command}}`

- 使用所有在输入和输出中出现的单词进行提示补全：

`rlwrap --remember {{command}}`

- 如果提示包含 ANSI 颜色代码，使用更好的提示补全：

`rlwrap --ansi-colour-aware {{command}}`

- 启用文件名补全（区分大小写）：

`rlwrap --complete-filenames {{command}}`

- 添加彩色提示，颜色名称或符合 ASCI 标准的颜色规格。使用大写的颜色名称以粗体样式显示：

`rlwrap --prompt-colour={{black|red|green|yellow|blue|cyan|purple|white|colour_spec}} {{command}}`