# cut

> 从 `stdin` 或文件中剪切字段。
> 更多信息：<https://keith.github.io/xcode-man-pages/cut.1.html>。

- 打印每行的特定字符/字段范围：

`{{command}} | cut -{{c|f}} {{1|1,10|1-10|1-|-10}}`

- 打印每行的字段范围，使用特定分隔符：

`{{command}} | cut -d "{{,}}" -f {{1}}`

- 打印特定文件每行的字符范围：

`cut -c {{1}} {{path/to/file}}`