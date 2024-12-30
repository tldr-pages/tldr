# 海绵

> 在写入输出文件之前先吸收输入。
> 更多信息：<https://manned.org/sponge>。

- 将文件内容追加到源文件：

`cat {{path/to/file}} | sponge -a {{path/to/file}}`

- 删除文件中以 # 开头的所有行：

`grep -v '^{{#}}' {{path/to/file}} | sponge {{path/to/file}}`