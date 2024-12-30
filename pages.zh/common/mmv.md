# mmv

> 批量移动和重命名文件。
> 更多信息：<https://manned.org/mmv.1>。

- 将所有具有特定扩展名的文件重命名为不同的扩展名：

`mmv "*{{.old_extension}}" "#1{{.new_extension}}"`

- 将 `report6part4.txt` 复制到 `./french/rapport6partie4.txt`，并同时复制所有同名文件：

`mmv -c "{{report*part*.txt}}" "{{./french/rapport#1partie#2.txt}}"`

- 将所有 `.txt` 文件合并为一个文件：

`mmv -a "{{*.txt}}" "{{all.txt}}"`

- 将文件名中的日期格式从 "M-D-Y" 转换为 "D-M-Y" 格式：

`mmv "{{[0-1][0-9]-[0-3][0-9]-[0-9][0-9][0-9][0-9].txt}}" "{{#3#4-#1#2-#5#6#7#8.txt}}"`