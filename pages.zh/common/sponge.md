# sponge

> 吸收输入内容后再写入输出文件。
> 更多信息：<https://manned.org/sponge>.

- 将文件内容追加到源文件：

`cat {{path/to/file}} | sponge -a {{path/to/file}}`

- 删除文件中所有以 # 开头的行：

`grep -v '^{{#}}' {{path/to/file}} | sponge {{path/to/file}}`