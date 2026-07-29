# truncate

> 将文件缩小或扩展到指定大小。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html>。

- 将现有文件设置为 10 GB，或创建指定大小的新文件：

`truncate {{[-s|--size]}} 10G {{路径/到/文件}}`

- 将文件大小扩展 50 MiB，用空洞填充（读取为零字节）：

`truncate {{[-s|--size]}} +50M {{路径/到/文件}}`

- 将文件缩小 2 GiB，从文件末尾移除数据：

`truncate {{[-s|--size]}} -2G {{路径/到/文件}}`

- 清空文件内容：

`truncate {{[-s|--size]}} 0 {{路径/到/文件}}`

- 清空文件内容，但如果文件不存在则不创建：

`truncate {{[-s|--size]}} 0 {{[-c|--no-create]}} {{路径/到/文件}}`
