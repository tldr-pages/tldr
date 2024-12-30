# textutil

> 操作各种格式的文本文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/textutil.1.html>。

- 显示关于 `foo.rtf` 的信息：

`textutil -info {{path/to/foo.rtf}}`

- 将 `foo.rtf` 转换为 `foo.html`：

`textutil -convert {{html}} {{path/to/foo.rtf}}`

- 将富文本转换为普通文本：

`textutil {{path/to/foo.rtf}} -convert {{txt}}`

- 将 `foo.txt` 转换为 `foo.rtf`，使用 Times 10 作为字体：

`textutil -convert {{rtf}} -font {{Times}} -fontsize {{10}} {{path/to/foo.txt}}`

- 加载当前目录中的所有 RTF 文件，连接其内容，并将结果写出为 `index.html`，HTML 标题设置为 "多个文件"：

`textutil -cat {{html}} -title "多个文件" -output {{path/to/index.html}} *.rtf`