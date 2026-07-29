# fmt

> 通过合并段落并将行宽限制为指定字符数（默认 75）来重新格式化文本文件。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/fmt-invocation.html>。

- 重新格式化文件：

`fmt {{路径/到/文件}}`

- 重新格式化文件，生成最多 `n` 个字符的输出行：

`fmt {{[-w|--width]}} {{n}} {{路径/到/文件}}`

- 重新格式化文件，不将短于指定宽度的行合并：

`fmt {{[-s|--split-only]}} {{路径/到/文件}}`

- 以统一间距重新格式化文件（单词之间 1 个空格，段落之间 2 个空格）：

`fmt {{[-u|--uniform-spacing]}} {{路径/到/文件}}`
