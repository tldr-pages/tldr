# 小于号

> 将数据重定向到 `stdin`。
> 更多信息：<https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>.

- 将文件重定向到 `stdin`（与 `cat file.txt |` 效果相同）:

`{{command}} < {{path/to/file.txt}}`

- 创建一个 here document 并将其传递给 `stdin`（需要多行命令）:

`{{command}} << {{EOF}} <Enter> {{multiline_data}} <Enter> {{EOF}}`

- 创建一个 here string 并将其传递给 `stdin`（与 `echo string |` 效果相同）:

`{{command}} <<< {{string}}`

- 从文件中读取数据并将其输出写入另一个文件:

`{{command}} < {{path/to/file.txt}} > {{path/to/file2.txt}}`

- 将 here document 写入文件:

`cat << {{EOF}} > {{path/to/file.txt}} <Enter> {{multiline_data}} <Enter> {{EOF}}`

- 忽略前导制表符（适用于带有缩进的脚本，但不适用于空格）:

`cat <<- {{EOF}} > {{path/to/file.txt}} <Enter> {{multiline_data}} <Enter> {{EOF}}`
