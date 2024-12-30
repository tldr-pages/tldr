# 截断

> 将文件的大小缩小或扩展到指定大小。
> 更多信息：<https://www.gnu.org/software/coreutils/truncate>。

- 将现有文件的大小设置为 10 GB，或创建一个指定大小的新文件：

`truncate --size 10G {{path/to/file}}`

- 将文件大小扩展 50 MiB，填充为零字节（读作零字节）：

`truncate --size +50M {{path/to/file}}`

- 将文件缩小 2 GiB，方法是从文件末尾删除数据：

`truncate --size -2G {{path/to/file}}`

- 清空文件内容：

`truncate --size 0 {{path/to/file}}`

- 清空文件内容，但如果文件不存在则不创建文件：

`truncate --no-create --size 0 {{path/to/file}}`