# textutil

> 用于操作各种格式的文本文件。
> 更多信息：<https://ss64.com/osx/textutil.html>.

- 显示有关 `foo.rtf` 的信息：

`textutil -info {{foo.rtf}}`

- 将 `foo.rtf` 转换为 `foo.html`：

`textutil -convert {{html}} {{foo.rtf}}`

- 将带格式的 rtf 文本转换为普通 txt 文本：

`textutil {{foo.rtf}} -convert {{txt}}`

- 将 `foo.txt` 转换为 `foo.rtf`, 字体使用 Times 字号 10：

`textutil -convert {{rtf}} -font {{Times}} -fontsize {{10}} {{foo.txt}}`

- 加载当前目录中的所有 RTF 文件，连接其内容，并将结果作为 `index.html` 写入，HTML 标题设置为"多个文件"：

`textutil -cat {{html}} -title "多个文件" -output {{index.html}} *.rtf`
