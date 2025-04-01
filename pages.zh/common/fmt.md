# fmt

> 通过合并段落并限制每行的字符数（默认为75）来重新格式化文本文件。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/fmt-invocation.html>.

- 重新格式化文件：

`fmt {{path/to/file}}`

- 重新格式化文件，输出每行最多 `n` 个字符：

`fmt {{[-w|--width]}} {{n}} {{path/to/file}}`

- 重新格式化文件，不将短于给定宽度的行合并在一起：

`fmt {{[-s|--split-only]}} {{path/to/file}}`

- 重新格式化文件，并使用统一间距（单词间1个空格，段落间2个空格）：

`fmt {{[-u|--uniform-spacing]}} {{path/to/file}}`
