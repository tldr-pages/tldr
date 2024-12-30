# 小于

> 将数据重定向到 `stdin`。
> 更多信息：<https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>。

- 将文件重定向到 `stdin`（效果与 `cat file.txt |` 相同）：

`{{command}} < {{path/to/file.txt}}`

- 创建一个 here 文档并将其传递到 `stdin`（需要多行命令）：

`{{command}} << {{EOF}} <Enter> {{multiline_data}} <Enter> {{EOF}}`

- 创建一个 here 字符串并将其传递到 `stdin`（效果与 `echo string |` 相同）：

`{{command}} <<< {{string}}`